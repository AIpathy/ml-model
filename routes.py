from fastapi import APIRouter

from data_types import (
    anksiyete_input, borderline_input, narsizm_input, sosyal_fobi_input,
    beck_depresyon_input, alkol_input, kayip_yas_input, travma_input,
    cocuk_terkedilme_input, coklu_zeka_input, dehb_input, ofke_sim_input,
    golombok_input, okb_input
)
from predictors import (
    predict_anksiyete, predict_borderline, predict_narsizm, predict_sosyal_fobi,
    predict_beck_depresyon, predict_alkol, predict_kayip_yas, predict_travma,
    predict_cocuk_terkedilme, predict_coklu_zeka, predict_dehb, predict_ofke_sim,
    predict_golombok, predict_okb
)
from lang_model import generate_response, stt_emotion

router = APIRouter()

@router.post("/predict_anksiyete/")
def predict_anksiyete_route(new_point: anksiyete_input):
    prediction = predict_anksiyete(new_point)
    ai_comment = generate_response("Anksiyete Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@router.post("/predict_borderline/")
def predict_borderline_route(new_point: borderline_input):
    prediction = predict_borderline(new_point)
    ai_comment = generate_response("Borderline Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@router.post("/predict_narsizm/")
def predict_narsizm_route(new_point: narsizm_input):
    prediction = predict_narsizm(new_point)
    ai_comment = generate_response("Narsizm Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@router.post("/predict_sosyal_fobi/")
def predict_sosyal_fobi_route(new_point: sosyal_fobi_input):
    prediction = predict_sosyal_fobi(new_point)
    ai_comment = generate_response("Sosyal Fobi Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@router.post("/predict_beck_depresyon/")
def predict_beck_depresyon_route(new_point: beck_depresyon_input):
    prediction = predict_beck_depresyon(new_point)
    ai_comment = generate_response("Beck Depresyon Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@router.post("/predict_alkol/")
def predict_alkol_route(new_point: alkol_input):
    prediction = predict_alkol(new_point)
    ai_comment = generate_response("Alkol Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@router.post("/predict_kayip_yas/")
def predict_kayip_yas_route(new_point: kayip_yas_input):
    prediction = predict_kayip_yas(new_point)
    ai_comment = generate_response("Kayıp(Yas) Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@router.post("/predict_travma/")
def predict_travma_route(new_point: travma_input):
    prediction = predict_travma(new_point)
    ai_comment = generate_response("Travma Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@router.post("/precit_cocuk_terkedilme/")
def predict_cocuk_terkedilme_route(new_point: cocuk_terkedilme_input):
    prediction = predict_cocuk_terkedilme(new_point)
    ai_comment = generate_response("Çocuk Terkedilme Testi", prediction)
    return {'Risk_Grubu': prediction, 'AI_Yorum': ai_comment}

@router.post("/predict_coklu_zeka/")
def predict_coklu_zeka_route(new_point: coklu_zeka_input):
    prediction = predict_coklu_zeka(new_point)
    ai_comment = generate_response("Çoklu Zeka Testi", prediction)
    return {'Baskın_Zeka': prediction, 'AI_Yorum': ai_comment}

@router.post("/predict_dehb/")
def predict_dehb_route(new_point: dehb_input):
    prediction = predict_dehb(new_point)
    ai_comment = generate_response("DEHB Testi", prediction)
    return {'Risk Grubu': prediction, 'AI_Yorum': ai_comment}

@router.post("/predict_ofke_sim/")
def predict_ofke_sim_route(new_point: ofke_sim_input):
    prediction = predict_ofke_sim(new_point)
    ai_comment = generate_response("Öfke Yönetimi Testi", prediction)
    return {'Risk Grubu': prediction, 'AI_Yorum': ai_comment}

@router.post("/predict_golombok/")
def predict_golombok_route(new_point: golombok_input):
    prediction = predict_golombok(new_point)
    ai_comment = generate_response("Golombok Testi", prediction)
    return {'Risk Grubu': prediction, 'AI_Yorum': ai_comment}

@router.post("/predict_okb/")
def predict_okb_route(new_point: okb_input):
    prediction = predict_okb(new_point)
    ai_comment = generate_response("OKB Testi", prediction)
    return {'Risk Grubu': prediction, 'AI_Yorum': ai_comment}

@router.post("/stt_emotion/")
def stt_emotion_route(audio_file_path: str):
    transcription = stt_emotion(audio_file_path)
    return {'Transcription': transcription}