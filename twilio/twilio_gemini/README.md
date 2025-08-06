Gemini Voice Assistant
This project is a Python-based voice assistant that uses Flask to serve a webhook, Twilio to handle phone calls, and the Gemini API for conversational AI. It can place outbound calls to a user and interact with them in real-time.

Prerequisites
Python 3.7+ installed on your system.

A Twilio account with an active phone number.

A Google Gemini API Key.

Ngrok to expose your local server to the internet.

Project Setup
Clone the repository to your local machine.

Create a virtual environment and activate it.

Install dependencies:

Bash

pip install -r requirements.txt

Create a .env file and populate it with your credentials. Do not commit this file to your repository. Create a .gitignore file with .env and .venv/ to prevent this.

.env File
Create a file named .env in your project directory with the following variables:

GEMINI_API_KEY="YOUR_GEMINI_API_KEY"
TWILIO_ACCOUNT_SID="YOUR_TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN="YOUR_TWILIO_AUTH_TOKEN"
TWILIO_PHONE_NUMBER="YOUR_TWILIO_PHONE_NUMBER"
YOUR_PHONE_NUMBER="YOUR_PERSONAL_PHONE_NUMBER"
NGROK_URL="YOUR_NGROK_URL"
Running the Application
Follow these steps in separate terminals.

Step 1: Start the Flask Server
Navigate to your project directory, activate your virtual environment, and run the Flask application.

Bash

# Navigate to your project directory

cd [your-project-directory]

# Activate the virtual environment

[your-venv-activation-command]

# Run the Flask server

python gemini_flask.py
Leave this terminal open and running.

Step 2: Start Ngrok
Navigate to the directory where your ngrok executable is located and start the tunnel.

Bash

# Navigate to ngrok directory

cd [your-ngrok-directory]

# Run ngrok to expose your local server

ngrok http 5000
Copy the new URL that ngrok provides. Leave this terminal open.

Step 3: Update .env and Make the Call
This is the final step. Run the calling script in a third terminal.

Before running the script, open your .env file and replace the NGROK_URL with the new URL you copied from Step 2.

Run the script to place the call.

Bash

# Navigate to your project directory

cd [your-project-directory]

# Activate the virtual environment

[your-venv-activation-command]

# This command will place the call to your phone

python gemini_calling.py
