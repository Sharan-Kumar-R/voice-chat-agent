import os
import requests
from dotenv import load_dotenv
import subprocess
import shutil
import time
from deepgram import Deepgram

# Load environment variables
load_dotenv()

# Set your Deepgram API Key and desired voice model
DG_API_KEY = os.getenv("DEEPGRAM_API_KEY")
MODEL_NAME = "aura-asteria-en"  # Example model name, change as needed

def is_installed(lib_name: str) -> bool:
    lib = shutil.which(lib_name)
    return lib is not None

def play_stream(audio_stream, use_ffmpeg=True):
    player = "ffplay"
    if not is_installed(player):
        raise ValueError(f"{player} not found, necessary to stream audio.")
    
    player_command = ["ffplay", "-autoexit", "-", "-nodisp"]
    player_process = subprocess.Popen(
        player_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    for chunk in audio_stream:
        if chunk:
            player_process.stdin.write(chunk)  # type: ignore
            player_process.stdin.flush()  # type: ignore
    
    if player_process.stdin:
        player_process.stdin.close()
    player_process.wait()

def send_tts_request(text):
    model = "aura-asteria-en"
    DEEPGRAM_URL = f"https://api.deepgram.com/v1/speak?model={model}&encoding=linear16&sample_rate=24000"

    headers = {
        "Authorization": f"Token {DG_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "text": text  # ✅ Only `text`, not `voice`
    }

    player_command = ["ffplay", "-autoexit", "-", "-nodisp"]
    player_process = subprocess.Popen(
        player_command,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    with requests.post(DEEPGRAM_URL, stream=True, headers=headers, json=payload) as r:
        if r.status_code != 200:
            print(f"Error: {r.status_code}")
            print(r.text)
            return

        start_time = time.time()
        first_byte_time = None

        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                if first_byte_time is None:
                    first_byte_time = time.time()
                    ttfb = int((first_byte_time - start_time) * 1000)
                    print(f"Time to First Byte (TTFB): {ttfb}ms")

                if player_process.stdin:
                    player_process.stdin.write(chunk)
                    player_process.stdin.flush()

    if player_process.stdin:
        player_process.stdin.close()
    player_process.wait()


# Get input from the user
text = input("Enter the text you want to convert to speech: ")
send_tts_request(text)