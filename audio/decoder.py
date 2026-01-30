import base64
import os

def base64_to_mp3(audio_base64: str, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    audio_bytes = base64.b64decode(audio_base64)
    with open(output_path, "wb") as f:
        f.write(audio_bytes)
