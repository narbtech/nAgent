# Twilio Audio Agent

### Project Description

This project demonstrates how to use the Twilio API to make a phone call and play a hosted audio file. It uses a simple Flask web server to serve the audio and a separate Python script to initiate the call. All sensitive and changing information, such as API keys and phone numbers, are securely managed using a `.env` file.

### Features

- Initiates a phone call using the Twilio API.
- Hosts and serves a local audio file using a lightweight Flask server.
- Uses a `.env` file to securely store and manage credentials.

### Prerequisites

- Python 3.x
- A Twilio Account and Phone Number
- The ngrok tool to expose your local Flask server to the internet.

### Setup Instructions

Follow these steps to get a copy of the project up and running on your local machine.

1.  **Clone the Repository**
    ```sh
    git clone https://github.com/narbtech/nAgent.git
    cd nAgent
    ```
2.  **Create a Python Virtual Environment**
    ```sh
    python -m venv venv
    ```
3.  **Activate the Virtual Environment**
    - **On Windows:**
      ```sh
      .\venv\Scripts\activate
      ```
    - **On macOS/Linux:**
      ```sh
      source venv/bin/activate
      ```
4.  **Install Dependencies**
    ```sh
    pip install -r requirements.txt
    ```
5.  **Set Up Environment Variables**

    - Create a new file named `.env` in the root of the project.
    - Add your Twilio credentials and other configurable information to this file:

      ```
      # Twilio Credentials
      TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
      TWILIO_AUTH_TOKEN="your_auth_token"
      TWILIO_PHONE_NUMBER="+1xxxxxxxxxx"
      TWILIO_TO_NUMBER="+1xxxxxxxxxx"

      # Other configurable values
      AUDIO_FILE="Gmas 3.wav"
      NGROK_URL="https://your-ngrok-url.ngrok-free.app"
      ```

6.  **Start the ngrok Tunnel**
    - Open a new terminal and start ngrok to expose your local server on port 5000:
      ```sh
      ngrok http 5000
      ```
    - Copy the "Forwarding" HTTPS URL and paste it into your `.env` file for the `NGROK_URL`.

### Usage

1.  **Start the Flask Server**
    - In your first terminal, make sure your virtual environment is active and run the Flask server:
      ```sh
      python flask_start.py
      ```
2.  **Initiate the Twilio Call**
    - In a new terminal, with your virtual environment active, run the Twilio script:
      ```sh
      python twilio_audio.py
      ```
