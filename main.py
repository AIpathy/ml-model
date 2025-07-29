# main.py
from fastapi import FastAPI, File, UploadFile
from data_types import anksiyete_input, borderline_input, narsizm_input, sosyal_fobi_input, beck_depresyon_input, alkol_input
from predictors import predict_anksiyete, predict_borderline, predict_narsizm, predict_sosyal_fobi, predict_beck_depresyon, predict_alkol
from lang_model import generate_response, stt_emotion
import uvicorn
import tempfile
import os


app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ML Model API is running!"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/predict_anksiyete/")
def predict_anksiyete_route(new_point: anksiyete_input):
    prediction = predict_anksiyete(new_point)
    ai_comment = generate_response("Anksiyete Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@app.post("/predict_borderline/")
def predict_borderline_route(new_point: borderline_input):
    prediction = predict_borderline(new_point)
    ai_comment = generate_response("Borderline Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@app.post("/predict_narsizm/")
def predict_narsizm_route(new_point: narsizm_input):
    prediction = predict_narsizm(new_point)
    ai_comment = generate_response("Narsizm Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@app.post("/predict_sosyal_fobi/")
def predict_sosyal_fobi_route(new_point: sosyal_fobi_input):
    prediction = predict_sosyal_fobi(new_point)
    ai_comment = generate_response("Sosyal Fobi Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@app.post("/predict_beck_depresyon/")
def predict_beck_depresyon_route(new_point: beck_depresyon_input):
    prediction = predict_beck_depresyon(new_point)
    ai_comment = generate_response("Beck Depresyon Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@app.post("/predict_alkol/")
def predict_alkol_route(new_point: alkol_input):
    prediction = predict_alkol(new_point)
    ai_comment = generate_response("Alkol Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@app.post("/stt_emotion/")
async def stt_emotion_route(audio_file: UploadFile = File(...)):
    # Geçici dosya oluştur
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(audio_file.filename)[1]) as temp_file:
        # Upload edilen dosyayı geçici dosyaya yaz
        content = await audio_file.read()
        temp_file.write(content)
        temp_file_path = temp_file.name
    
    try:
        transcription = stt_emotion(temp_file_path)
        return {'Transcription': transcription}
    finally:
        # Geçici dosyayı temizle
        if os.path.exists(temp_file_path):
            os.unlink(temp_file_path)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)