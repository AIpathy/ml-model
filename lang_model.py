from google import genai
from google.genai import types
import os
from dotenv import load_dotenv
from io import BytesIO
import requests
from elevenlabs.client import ElevenLabs

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

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
    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
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