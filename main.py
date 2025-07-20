import pandas as pd
import pickle

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class anksiyete_input(BaseModel):
    Yas: int
    Cinsiyet: str
    Medeni_Hal: str
    Is_Durumu: str
    Egitim: str
    Gelir_Duzeyi: str
    Yasam_Yeri: str
    Psikolojik_Destek: str
    Calisma_Suresi: int
    Soru_1: int
    Soru_2: int
    Soru_3: int
    Soru_4: int
    Soru_5: int
    Soru_6: int
    Soru_7: int
    Soru_8: int
    Soru_9: int
    Soru_10: int
    Soru_11: int
    Soru_12: int
    Soru_13: int
    Soru_14: int
    Soru_15: int
    Soru_16: int
    Soru_17: int
    Soru_18: int
    Soru_19: int
    Soru_20: int

@app.post("/predict_anksiyete/")
def predict_anksiyete(new_point : anksiyete_input):
    encoder_path = './encoders/anksiyete_rf_encoder.pkl'
    model_path = './models/anksiyete_rf_model.pkl'

    new_point = new_point.model_dump()
    #print(new_point)

    new_data = pd.DataFrame([new_point])
    
    # Load the saved encoder
    with open(encoder_path, 'rb') as f:
        encoder = pickle.load(f)

    # Load the saved model
    with open(model_path, 'rb') as f:
        model = pickle.load(f)

    # Select only the same categorical columns used during training
    categorical_cols = new_data.select_dtypes(include=['object', 'category']).columns

    # Encode the categorical part
    encoded_new_cat = encoder.transform(new_data[categorical_cols])

    # Convert to DataFrame
    encoded_new_cat_df = pd.DataFrame(encoded_new_cat, columns=encoder.get_feature_names_out(categorical_cols), index=new_data.index)

    # Drop original categorical columns and concatenate encoded ones
    new_data_encoded = pd.concat([encoded_new_cat_df,new_data.drop(columns=categorical_cols)], axis=1)

    prediction = model.predict(new_data_encoded)

    return {'Risk_Grubu' : prediction[0]}


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

