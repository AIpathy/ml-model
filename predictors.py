# predictor.py
import pandas as pd
import pickle

def predict_anksiyete(new_point):
    encoder_path = '/app/encoders/anksiyete_rf_encoder.pkl'
    model_path = '/app/models/anksiyete_rf_model.pkl'

    new_point = new_point.model_dump()
    soru_list = new_point.pop('sorular', None)
    for i in range(1, 21):
        soru_key = f'Soru_{i}'
        new_point[soru_key] = soru_list[i-1] if soru_list else 0
    
    # Convert the input to a DataFrame
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
    new_data_encoded = pd.concat([encoded_new_cat_df, new_data.drop(columns=categorical_cols)], axis=1)

    # Make prediction
    prediction = model.predict(new_data_encoded)

    return prediction[0]

def predict_borderline(new_point):
    encoder_path = '/app/encoders/borderline_rf_encoder.pkl'
    model_path = '/app/models/borderline_rf_model.pkl'

    new_point = new_point.model_dump()
    soru_list = new_point.pop('sorular', None)
    for i in range(1, 54):
        soru_key = f'Soru_{i}'
        new_point[soru_key] = soru_list[i-1] if soru_list else 0
    
    # Convert the input to a DataFrame
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
    new_data_encoded = pd.concat([encoded_new_cat_df, new_data.drop(columns=categorical_cols)], axis=1)

    # Make prediction
    prediction = model.predict(new_data_encoded)

    return prediction[0]

def predict_narsizm(new_point):
    encoder_path = '/app/encoders/narsizm_rf_encoder.pkl'
    model_path = '/app/models/narsizm_rf_model.pkl'

    new_point = new_point.model_dump()
    soru_list = new_point.pop('sorular', None)
    for i in range(1, 26):
        soru_key = f'Soru_{i}'
        new_point[soru_key] = soru_list[i-1] if soru_list else 0
    
    # Convert the input to a DataFrame
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
    new_data_encoded = pd.concat([encoded_new_cat_df, new_data.drop(columns=categorical_cols)], axis=1)

    # Make prediction
    prediction = model.predict(new_data_encoded)

    return prediction[0]

def predict_sosyal_fobi(new_point):
    encoder_path = '/app/encoders/sosyal_fobi_rf_encoder.pkl'
    model_path = '/app/models/sosyal_fobi_rf_model.pkl'

    new_point = new_point.model_dump()
    soru_list = new_point.pop('sorular', None)
    for i in range(1, 46):
        soru_key = f'Soru_{i}'
        new_point[soru_key] = soru_list[i-1] if soru_list else 0
    
    # Convert the input to a DataFrame
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
    new_data_encoded = pd.concat([encoded_new_cat_df, new_data.drop(columns=categorical_cols)], axis=1)

    # Make prediction
    prediction = model.predict(new_data_encoded)

    return prediction[0]

def predict_alkol(new_point):
    encoder_path = '/app/encoders/alkol_testi_rf_encoder.pkl'
    model_path = '/app/models/alkol_testi_rf_model.pkl'

    new_point = new_point.model_dump()
    soru_list = new_point.pop('sorular', None)
    for i in range(1, 35):
        soru_key = f'Soru_{i}'
        new_point[soru_key] = soru_list[i-1] if soru_list else 0
    
    # Convert the input to a DataFrame
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
    new_data_encoded = pd.concat([encoded_new_cat_df, new_data.drop(columns=categorical_cols)], axis=1)

    # Make prediction
    prediction = model.predict(new_data_encoded)

    return prediction[0]

def predict_beck_depresyon(new_point):
    encoder_path = '/app/encoders/beck_depresyon_rf_encoder.pkl'
    model_path = '/app/models/beck_depresyon_rf_model.pkl'

    new_point = new_point.model_dump()
    soru_list = new_point.pop('sorular', None)
    for i in range(1, 22):
        soru_key = f'Soru_{i}'
        new_point[soru_key] = soru_list[i-1] if soru_list else 0
    
    # Convert the input to a DataFrame
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
    new_data_encoded = pd.concat([encoded_new_cat_df, new_data.drop(columns=categorical_cols)], axis=1)

    # Make prediction
    prediction = model.predict(new_data_encoded)

    return prediction[0]