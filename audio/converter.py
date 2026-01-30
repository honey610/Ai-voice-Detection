# from pydub import AudioSegment

# def mp3_to_wav(mp3_path: str, wav_path: str):
#     audio = AudioSegment.from_mp3(mp3_path)
#     audio.export(wav_path, format="wav")

# import subprocess
# import os

# FFMPEG_PATH = r"C:\ffmpeg-8.0.1-essentials_build\bin\ffmpeg.exe"

# def mp3_to_wav(mp3_path: str, wav_path: str):
#     os.makedirs(os.path.dirname(wav_path), exist_ok=True)

#     command = [
#         FFMPEG_PATH,
#         "-y",                 # overwrite
#         "-i", mp3_path,
#         "-ac", "1",           # mono
#         "-ar", "16000",       # 16kHz
#         wav_path
#     ]

#     subprocess.run(command, check=True)

import subprocess

def mp3_to_wav(mp3_path, wav_path):
    command = [
        "ffmpeg",           # ✅ NO hardcoded path
        "-y",
        "-i", mp3_path,
        "-ac", "1",
        "-ar", "16000",
        wav_path
    ]
    subprocess.run(command, check=True)

