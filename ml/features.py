import librosa
import numpy as np

def extract_features(wav_path: str):
    y,sr=librosa.load(wav_path,sr=16000)
    energy = np.mean(librosa.feature.rms(y=y))
    energy_var = np.var(librosa.feature.rms(y=y))
    zcr = np.mean(librosa.feature.zero_crossing_rate(y))
    spec_flatness = np.mean(librosa.feature.spectral_flatness(y=y))
    return {
        "energy": energy,
        "energy_var": energy_var,
        "zcr": zcr,
        "spectral_flatness": spec_flatness
    }