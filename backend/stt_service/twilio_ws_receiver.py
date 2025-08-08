'''
 - Handles connection to deepgram
 - Turns twilio json into readable data for deepgrams
'''

import asyncio
import base64
import json
import websockets
import sys, pathlib
backend_service_dir = pathlib.Path(__file__).resolve().parents[1] / "backend" / "stt_service"
sys.path.insert(0, str(backend_service_dir))
from stt import deepgram_connection

async def handle_twilio_stream(websocket):
    print("Twilio Call Connected.")
    dg_ws = await deepgram_connection()

    try:
        async for message in websocket:
            data = json.loads(message)
            if data.get("event") == "media":
                audio_b64 = data["media"]["payload"]
                audio_bytes = base64.b64decode(audio_b64)
                await dg_ws.send(audio_bytes)
    except Exception as e:
        print("Error.", e)
    finally:
        await dg_ws.send("")
        await dg_ws.close()
        print("Call Ended.")
    
async def main():
    async with websockets.serve(handle_twilio_stream, "0.0.0.0", 8765):
        print("WebSocket server listening on :8765")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())

