from flask import Flask, send_file
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)


@app.route("/audio")
def serve_audio():
    # Get the filename from the environment variable
    audio_file_name = os.getenv("AUDIO_FILE")

    # You can add a check here in case the variable is not set
    if not audio_file_name:
        return "Error: AUDIO_FILE not configured.", 500

    return send_file(audio_file_name, mimetype="audio/wav")


if __name__ == "__main__":
    # Get the port from the environment variable, or use a default if not set
    port = int(os.getenv("PORT", 5000))
    app.run(port=port)
