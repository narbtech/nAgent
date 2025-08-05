from twilio.rest import Client
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials and phone numbers from env variables. Fill these in .env with your personal info
# AUDIO_FILE=".wav"
# TWILIO_ACCOUNT_SID=""
# TWILIO_AUTH_TOKEN=""
# TWILIO_PHONE_NUMBER="+1..."
# TWILIO_TO_NUMBER="+1..."
# NGROK_URL=""
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
twilio_phone_number = os.getenv("TWILIO_PHONE_NUMBER")
to_number = os.getenv("TWILIO_TO_NUMBER")
ngrok_url = os.getenv("NGROK_URL")

# Make sure the required variables are set
if not all([account_sid, auth_token, twilio_phone_number, to_number, ngrok_url]):
    print("Error: One or more required environment variables are not set.")
    exit()

client = Client(account_sid, auth_token)

call = client.calls.create(
    to=to_number,
    from_=twilio_phone_number,
    twiml=f"""
        <Response>
            <Play>{ngrok_url}/audio</Play>
            <Pause length="30"/>
        </Response>
    """,
)

print(f"Call initiated with SID: {call.sid}")
