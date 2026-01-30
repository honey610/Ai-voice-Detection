def classify(features):
    score=0
    if features["energy_var"]<0.0005:
        score+=0.3
    if features["spectral_flatness"] > 0.25:
        score += 0.4

    if features["zcr"] < 0.05:
        score += 0.3

    confidence = min(score, 1.0)
    if confidence > 0.5:
        return {
            "classification": "AI_GENERATED",
            "confidence": round(confidence, 2),
            "explanation": "Low energy variation and flat spectral profile suggest synthetic speech."
        }
    else:
        return {
            "classification": "HUMAN",
            "confidence": round(1 - confidence, 2),
            "explanation": "Natural energy fluctuations and spectral richness indicate human speech."
        }