import librosa
import soundfile as sf

def normalize_audio(wav_path: str, output_path: str):
    y, sr = librosa.load(wav_path, sr=16000, mono=True)
    sf.write(output_path, y, 16000)