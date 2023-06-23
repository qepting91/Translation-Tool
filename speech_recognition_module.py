import os
import speech_recognition as sr
import logging

class SpeechRecognitionModule:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.logger = logging.getLogger(__name__)

    def transcribe_speech(self, audio_file_path, language='ru-RU'):
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError(f"File not found: {audio_file_path}")

        with sr.AudioFile(audio_file_path) as source:
            audio = self.recognizer.record(source)

        try:
            transcribed_text = self.recognizer.recognize_google(audio, language=language)
        except sr.UnknownValueError:
            self.logger.error("Google Speech Recognition could not understand audio")
            transcribed_text = "Unable to transcribe speech"
        except sr.RequestError as e:
            self.logger.error("Could not request results from Google Speech Recognition service; {0}".format(e))
            transcribed_text = "Unable to transcribe speech"

        return transcribed_text

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    module = SpeechRecognitionModule()
    try:
        # Replace 'audio.wav' with the path to the audio file you want to transcribe.
        transcribed_text = module.transcribe_speech('audio.wav', language='en-US')  # added language parameter here
        print(f"Transcribed text: {transcribed_text}")
    except Exception as e:
        logging.error(f"Failed to transcribe audio: {str(e)}")
