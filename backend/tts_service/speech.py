import time
import sys
import os

# Add the backend directory to Python path to find config module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import config
from groq import Groq

client = Groq(api_key=config.GROQ_API_KEY)

speech_file_path = "speech.wav"
model = "playai-tts"
voice = "Mason-PlayAI"
text = "Let me check"
response_format = "wav"

start_time = time.time()

response = client.audio.speech.create(
    model=model,
    voice=voice,
    input=text,
    response_format=response_format
)

end_time = time.time()

# here saves the audio file
response.write_to_file(speech_file_path)

# here it tells how long it took to process your text input
print(f"Time to generate voice: {end_time - start_time:.3f} seconds")
