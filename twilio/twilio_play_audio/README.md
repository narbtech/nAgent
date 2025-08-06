Twilio Play Audio
This project is a simple Python application that uses Flask and Twilio to place an outbound call and play an audio file to the recipient.

Prerequisites
Python 3.7+ installed on your system.

A Twilio account with an active phone number.

Ngrok to expose your local server to the internet.

Project Setup
Clone the repository to your local machine.

Create a virtual environment and activate it.

Install dependencies using the requirements file:

pip install -r requirements.txt

Create a .env file and populate it with your credentials. Do not commit this file to your repository.

.env File
Create a file named .env in your project directory with the following variables:

TWILIO_ACCOUNT_SID="YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN="YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER="YOUR_TWILIO_PHONE_NUMBER"
NGROK_URL="YOUR_NGROK_URL"
MY_PHONE_NUMBER="YOUR_PERSONAL_PHONE_NUMBER"

Running the Application
Follow these steps in separate terminals.

Step 1: Start the Flask Server
Navigate to your project directory, activate your virtual environment, and run the Flask application.

python flask_start.py

Leave this terminal open and running.

Step 2: Start Ngrok
Navigate to the directory where your ngrok executable is located and start the tunnel.

ngrok http 5000

Copy the new URL that ngrok provides and paste it into your .env file. Leave this terminal open.

Step 3: Make the Call
Run the calling script in a third terminal.

python twilio_audio.py

Your phone should ring, and when you answer, the audio file will play.
