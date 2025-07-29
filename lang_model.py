from google import genai
from google.genai import types
import os
from io import BytesIO
import requests
from elevenlabs import ElevenLabs
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Only run this block for Gemini Developer API
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY"),
    http_options=types.HttpOptions(api_version='v1alpha')
)

def generate_response(test_name, result):
    """
    Generates a response based on the test name and result using Google Gemini.
    
    Args:
        test_name (str): The name of the psychological test.
        result (str): The result of the test.
    
    Returns:
        str: The generated response text.
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        config= types.GenerateContentConfig(
            system_instruction="You are a helpful psychological assistant. " +
            "You will be given a test result about a psychological problem. " +
            "Your task is to respond according to this result." +
            "Give your answers in Turkish. "
        ),
        contents=f"Here is the result of the {test_name}: {result}" +
        "Comment about the test and the result" + 
        "Give your answer in Turkish."
    )
    return response.text



def stt_emotion(audio_file):
    load_dotenv()

    elevenlabs = ElevenLabs(
    api_key=os.getenv("ELEVENLABS_API_KEY"),
    )

    # Path to your local MP3 file
    audio_path = audio_file

    # Open the file and read the content
    with open(audio_path, 'rb') as f:
        audio_data = BytesIO(f.read())

    transcription = elevenlabs.speech_to_text.convert(
        file=audio_data,
        model_id="scribe_v1", # Model to use, for now only "scribe_v1" is supported
        tag_audio_events=True, # Tag audio events like laughter, applause, etc.
        language_code="tur", # Language of the audio file. If set to None, the model will detect the language automatically.
    )

    print(transcription)
    
    client = genai.Client()

    response = client.models.generate_content(
        model="gemini-2.5-flash", 
        config= types.GenerateContentConfig(
            system_instruction="You are a helpful assistant. " +
            "You will be given a transcription of an audio file. " +
            "Your task is to evaluate the mood of the person talking and support them if they need" +
            "Give your answers in Turkish. "
        ),
        contents=f"Here is the transcription of the audio file: {transcription.text}" +
        "Please evaluate the mood of the person talking in the audio file. Do not comment about this" +  
        "And support them if they are in a bad mood. " +
        "If they are in a good mood, you can just say that they are in a good mood. " +
        "If they are in a bad mood, you can suggest them to talk to a psychologist. " +
        "Give your answer in Turkish."
    )
    return(response.text)

def generate_chat_response(user_message):
    """
    Generates a chat response using Google Gemini.
    
    Args:
        user_message (str): The user's message.
    
    Returns:
        str: The generated response text.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash", 
            config=types.GenerateContentConfig(
                system_instruction="Sen yardımcı bir psikolojik asistanısın. " +
                "Kullanıcıların psikolojik durumları hakkında konuşmak için sana mesaj gönderiyorlar. " +
                "Görevlerin: " +
                "1. Empatik ve destekleyici ol " +
                "2. Profesyonel psikolojik tavsiye verme, sadece destek ol " +
                "3. Gerektiğinde bir psikoloğa danışmayı öner " +
                "4. Türkçe yanıt ver " +
                "5. Kısa ve öz yanıtlar ver " +
                "6. Kullanıcının duygusal durumunu anlamaya çalış "
            ),
            contents=f"Kullanıcı mesajı: {user_message}\n\nBu mesaja uygun, destekleyici bir yanıt ver."
        )
        return response.text
    except Exception as e:
        print(f"Gemini API error: {e}")
        # Fallback yanıt
        return "Mesajınızı aldım. Size nasıl yardımcı olabilirim? Psikolojik durumunuz hakkında konuşmak ister misiniz?"