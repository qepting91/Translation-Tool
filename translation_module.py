import logging
from google.cloud import translate_v2 as translate
import os
import config

class TranslationModule:
    def __init__(self):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = config.GOOGLE_APPLICATION_CREDENTIALS
        self.client = translate.Client()
        self.logger = logging.getLogger(__name__)

    def translate_text(self, text, source_language, target_language):
        try:
            result = self.client.translate(text, source_language=source_language, target_language=target_language)
            translation = result['translatedText']
        except Exception as e:
            self.logger.error(f"An error occurred while translating text: {str(e)}")
            raise

        return translation

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    module = TranslationModule()
    try:
        translation = module.translate_text("Hello, world!", "en", "fr")
        print(translation)
    except Exception as e:
        logging.error(f"Failed to translate text: {str(e)}")
