import os
import logging
from google.cloud import texttospeech
import config

class TextToSpeechModule:
    def __init__(self):
        self.credentials_file = config.GOOGLE_APPLICATION_CREDENTIALS
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.credentials_file
        self.client = None

    def authenticate(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = self.credentials_file
        self.client = texttospeech.TextToSpeechClient()

    def synthesize_speech(self, text, language_code='en-US'):
        if self.client is None:
            self.authenticate()

        # If no specific voice name is provided, use a default one based on the language
        voice_name = f"{language_code}-Standard-A"

        input_text = texttospeech.SynthesisInput(text=text)
        voice_params = texttospeech.VoiceSelectionParams(
            language_code=language_code,
            name=voice_name
        )
        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.LINEAR16
        )

        try:
            response = self.client.synthesize_speech(
                input=input_text,
                voice=voice_params,
                audio_config=audio_config
            )
        except Exception as e:
            logging.error(f"An error occurred while synthesizing speech: {str(e)}")
            raise e

        return response.audio_content