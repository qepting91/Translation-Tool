import logging
from tkinter import Tk
from gui_module import GuiModule
from translation_module import TranslationModule
from text_to_speech_module import TextToSpeechModule
from speech_recognition_module import SpeechRecognitionModule

class Main:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.gui = GuiModule(self.handle_gui_event)
        self.translator = TranslationModule()
        self.text_to_speech = TextToSpeechModule()
        self.speech_recognition = SpeechRecognitionModule()

    def run(self):
        self.logger.info("Application started")
        self.gui.run()

    def handle_gui_event(self, event, data):
        try:
            if event == 'translate_text':
                self.gui.display_translated_text(self.translator.translate_text(data['text'], data['source_lang'], data['target_lang']))
            elif event == 'convert_text_to_speech':
                self.gui.play_audio(self.text_to_speech.synthesize_speech(data['text'], language_code=data['target_lang']))
            elif event == 'transcribe_speech':
                self.gui.display_translated_text(self.speech_recognition.transcribe_speech(data['audio_file'], language='en-US'))
            elif event == 'generate_response':
                self.gui.display_generated_response(self.response_generator.generate_response(data['prompt']))
        except Exception as e:
            self.logger.error(f"An error occurred: {str(e)}")
            self.gui.display_error_message(str(e))

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    root = Tk()
    root.withdraw()
    main = Main()
    main.run()