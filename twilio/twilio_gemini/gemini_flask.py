# connect to Gemini in the phone call
import os
from flask import Flask, request
from twilio.twiml.voice_response import VoiceResponse, Gather, Say
from dotenv import load_dotenv
import json

# Import Google Generative AI SDK
from google.generativeai import GenerativeModel, configure
from google.generativeai.types import (
    GenerateContentResponse,
)  # Still useful for type checking if needed

# Load environment variables from .env file
load_dotenv()

# --- Configuration ---
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Google Generative AI with your API key
configure(api_key=GEMINI_API_KEY)
# Initialize the Gemini model
model = GenerativeModel("gemini-2.5-flash-preview-05-20")

# Initialize Flask app
app = Flask(__name__)

# A simple in-memory store for conversation context (for a real app, use a database like Firestore)
conversation_contexts = {}


# --- LLM Interaction Function ---
async def get_llm_response(caller_id, user_speech):
    """
    This function will interact with the LLM API using generate_content.
    It takes the caller_id to manage conversation history and the user's speech.
    """
    global conversation_contexts

    # Retrieve or initialize conversation context for this caller
    if caller_id not in conversation_contexts:
        # Initialize with a simple, non-themed system instruction
        conversation_contexts[caller_id] = {
            "history": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": "You are an AI assistant. Be helpful, concise, and friendly. Answer questions based on the conversation history. Do not use conversational chitchat or engage in topics unrelated to the user's direct questions."
                        }
                    ],
                }
            ]
        }

    context = conversation_contexts[caller_id]
    llm_response_text = ""

    # Add user's latest input to history
    if user_speech:
        context["history"].append({"role": "user", "parts": [{"text": user_speech}]})
    else:
        # Initial prompt for the very first turn of the conversation
        context["history"].append(
            {
                "role": "user",
                "parts": [{"text": "Greet the user and ask how you can help."}],
            }
        )

    print(
        f"LLM Prompt (User's last input): {user_speech if user_speech else 'Initial Call'}"
    )
    print(f"Current History for {caller_id}: {context['history']}")

    try:
        # --- ACTUAL GEMINI API CALL using generate_content ---
        response = model.generate_content(context["history"])

        # Check for an empty response or a safety-related finish reason
        if not response.candidates:
            finish_reason = (
                response.candidates[0].finish_reason
                if response.candidates
                else "unknown"
            )
            print(
                f"Gemini API returned an empty response with finish reason: {finish_reason}"
            )
            # The simplified prompt should prevent this, but the fallback is here just in case.
            llm_response_text = (
                "I'm having trouble processing your request. Please try again."
            )
        else:
            llm_response_text = response.text
            print(f"Gemini Response: {llm_response_text}")

        # Add LLM's response to history for the next turn
        context["history"].append(
            {"role": "model", "parts": [{"text": llm_response_text}]}
        )

    except Exception as e:
        print(f"Error interacting with LLM: {e}")
        llm_response_text = "I apologize, but I'm having trouble processing your request right now. Please try again later."

    return llm_response_text


# --- Twilio Webhook Endpoint ---
@app.route("/voice", methods=["GET", "POST"])
async def voice():
    """
    Handles incoming Twilio voice webhooks.
    """
    response = VoiceResponse()

    # Get parameters from Twilio's request
    call_sid = request.values.get("CallSid", None)
    speech_result = request.values.get(
        "SpeechResult", ""
    ).lower()  # Transcribed speech from Twilio

    print(f"Received Twilio webhook for Call SID: {call_sid}")
    print(f'Speech Result from Twilio: "{speech_result}"')

    # Get response from LLM
    llm_text_to_speak = await get_llm_response(call_sid, speech_result)

    # Speak the LLM's response
    response.say(llm_text_to_speak, voice="woman", language="en-US")

    # Keep gathering more speech for the next turn
    response.gather(
        input="speech", speech_timeout="auto", action="/voice", language="en-US"
    )

    # If no speech is detected after the prompt, hang up (fallback)
    response.say("I didn't hear anything. Goodbye!")
    response.hangup()

    return str(response)


# --- Server Start ---
if __name__ == "__main__":
    if not GEMINI_API_KEY:
        print(
            "ERROR: GEMINI_API_KEY is not set in your .env file. LLM interaction will NOT work."
        )
        print(
            "Please get your API key from https://aistudio.google.com/app/apikey and add it to your .env file."
        )
        exit()

    app.run(debug=True, port=5000)
    print(f"Flask server running on http://localhost:5000")
    print(
        "Remember to start Ngrok and configure your Twilio number's Voice URL to your Ngrok URL + /voice"
    )
