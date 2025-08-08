""" 
Real time STT from microphone using deepgram API:
 - Now accepts audio chunks externally through twilio
 - Sends to Deepgrams
 - Prints finalized transcriptions

"""

import os
import asyncio
import json
import websockets
from dotenv import load_dotenv
from websockets.legacy.client import connect

load_dotenv()

DG_API_KEY = os.getenv("DEEPGRAM_API_KEY")

SAMPLE_RATE = 16_000
CHUNK_MS = 100
CHUNK_SIZE = SAMPLE_RATE * CHUNK_MS // 1000 # samples per chunk

WS_URL = (
    "wss://api.deepgram.com/v1/listen"
    "?encoding=mulaw"
    "&sample_rate=8000"
    "&channels=1"
    "&punctuate=true"
    "&interim_results=true"
)

# open websocket to deepgram and returns connection
async def deepgram_connection():
    ws = await connect(
        WS_URL,
        extra_headers={"Authorization": f"Token {DG_API_KEY}"},
        ping_interval=5,
        ping_timeout=20,
        close_timeout=0,
    )
    print("Connected to Deepgram.")
    asyncio.create_task(receive_transcripts(ws))
    return ws

# listen for messages from deepgram, parses JSON and prints final transcript
async def receive_transcripts(ws) -> None:
    try:
        async for message in ws:
            try: 
                data = json.loads(message)

                if not data.get("speech_final", False) and not data.get("is_final", False):
                    continue 
                transcript = (
                    data["channel"]["alternatives"][0].get("transcript","")
                )
                if transcript.strip():
                    print(transcript)
            except (json.JSONDecodeError, KeyError):
                continue
    except (websockets.ConnectionClosedOK, websockets.ConnectionClosedError, asyncio.CancelledError):
        pass


