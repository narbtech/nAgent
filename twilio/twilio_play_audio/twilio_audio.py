# twilio_audio.py
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

# --- Configuration ---
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
NGROK_URL = os.getenv("NGROK_URL")
MY_PHONE_NUMBER = os.getenv("MY_PHONE_NUMBER")

# Initialize Twilio Client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

try:
    print(f"Calling {MY_PHONE_NUMBER} with TwiML from {NGROK_URL}/voice")
    call = client.calls.create(
        twiml=f'<Response><Redirect method="POST">{NGROK_URL}/voice</Redirect></Response>',
        to=MY_PHONE_NUMBER,
        from_=TWILIO_PHONE_NUMBER,
    )
    print(f"Call SID: {call.sid}")
except Exception as e:
    print(f"Error making call: {e}")
