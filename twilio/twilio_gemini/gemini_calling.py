import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# Your Account SID and Auth Token from twilio.com/console
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

# The URL of your running Flask app
NGROK_URL = os.getenv("NGROK_URL")

# Your phone number to receive the call
YOUR_PHONE_NUMBER = os.getenv("YOUR_PHONE_NUMBER")

if not all(
    [
        TWILIO_ACCOUNT_SID,
        TWILIO_AUTH_TOKEN,
        TWILIO_PHONE_NUMBER,
        NGROK_URL,
        YOUR_PHONE_NUMBER,
    ]
):
    print(
        "ERROR: Missing one or more environment variables. Please check your .env file."
    )
    exit()

client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

try:
    print(f"Calling {YOUR_PHONE_NUMBER} with TwiML from {NGROK_URL}/voice")
    call = client.calls.create(
        twiml=f'<Response><Say>Please wait while I connect you to the AI assistant.</Say><Redirect method="POST">{NGROK_URL}/voice</Redirect></Response>',
        to=YOUR_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
    )
    print(f"Call SID: {call.sid}")
except Exception as e:
    print(f"Error making call: {e}")
