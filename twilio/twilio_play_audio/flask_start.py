# flask_start.py
import os
from flask import Flask, request, url_for
from twilio.twiml.voice_response import VoiceResponse, Play
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# --- Configuration ---
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
NGROK_URL = os.getenv("NGROK_URL")

# Initialize Flask app
app = Flask(__name__)


# --- Twilio Webhook Endpoint ---
@app.route("/voice", methods=["GET", "POST"])
def voice():
    response = VoiceResponse()
    response.play(url=url_for("static", filename="Gmas 3.wav", _external=True))
    return str(response)


# --- Server Start ---
if __name__ == "__main__":
    if not all([TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER]):
        print("ERROR: Missing Twilio credentials. Please check your .env file.")
        exit()
    app.run(debug=True, port=5000)
