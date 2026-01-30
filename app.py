from fastapi import FastAPI, HTTPException,Depends
from auth.api_key import verify_api_key
from pydantic import BaseModel
import uuid
import os

from audio.decoder import base64_to_mp3
from audio.converter import mp3_to_wav
from ml.features import extract_features
from ml.classifier import classify




app = FastAPI(title="Audio Conversion Service")

# ---------- Request Schema ----------
class ConvertRequest(BaseModel):
    audio_format: str = "mp3"
    audio_base64: str




# ---------- Response Schema ----------
# class ConvertResponse(BaseModel):
#     status: str
#     wav_path: str
class DetectResponse(BaseModel):
    classification: str
    confidence: float
    explanation: str


# ---------- Endpoint ----------
@app.post("/convert", response_model=DetectResponse)
def convert_audio(payload: ConvertRequest, _: bool = Depends(verify_api_key)):
    if payload.audio_format != "mp3":
        raise HTTPException(status_code=400, detail="Only mp3 supported")

    if len(payload.audio_base64) < 1000:
        raise HTTPException(status_code=400, detail="Invalid audio data")
     

    uid = str(uuid.uuid4())
    mp3_path = f"temp/{uid}.mp3"
    wav_path = f"temp/{uid}.wav"

    try:
        base64_to_mp3(payload.audio_base64, mp3_path)
        mp3_to_wav(mp3_path, wav_path)
        features = extract_features(wav_path)
        result = classify(features)
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(mp3_path):
            os.remove(mp3_path)

    
    