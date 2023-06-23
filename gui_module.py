import logging
import tkinter as tk
from tkinter import messagebox, filedialog
import os
import pygame
from text_to_speech_module import TextToSpeechModule

class GuiModule:
    def __init__(self, event_handler):
        self.logger = logging.getLogger(__name__)
        self.event_handler = event_handler
        self.audio_file_path = None
        pygame.mixer.init()

        self.root = tk.Tk()
        self.root.title("Translation App")
        self.root.geometry("1000x1000")

        self.languages = [
            ('English', 'en-US'),
            ('Russian', 'ru-RU'),
            ('Belarusian', 'be-BY'),
            ('Ukrainian', 'uk-UA'),
            ('Uzbek', 'uz-UZ'),
            ('Armenian', 'hy-AM'),
            ('Azerbaijani', 'az-AZ'),
            ('Kazakh', 'kk-KZ'),
            ('Kyrgyz', 'ky-KG'),
            ('Tajik', 'tg-TJ'),
            ('Turkmen', 'tk-TM'),
            ('Moldavian', 'ro-MD'),  # Moldova primarily speaks Romanian
            ('Mandarin Chinese', 'zh-CN'),  # Mainland China
            ('Cantonese Chinese', 'yue-Hant-HK'),  # Hong Kong
        ]

        self.source_lang = tk.StringVar(self.root)
        self.target_lang = tk.StringVar(self.root)
        self.create_widgets()

        self.text_to_speech_module = TextToSpeechModule()

    def create_widgets(self):
        # Input and Output section
        input_frame = tk.Frame(self.root)
        input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        output_frame = tk.Frame(self.root)
        output_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.input_label = self.create_label(input_frame, "Input Text:")
        self.input_text = self.create_text_area(input_frame)

        self.output_label = self.create_label(output_frame, "Output Text:")
        self.output_text = self.create_text_area(output_frame)

        # Source and Target language selection
        language_frame = tk.Frame(self.root)
        language_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.source_lang_label = self.create_label(language_frame, "Source Language:")
        self.source_lang_menu = self.create_language_dropdown(language_frame, self.source_lang)

        self.target_lang_label = self.create_label(language_frame, "Target Language:")
        self.target_lang_menu = self.create_language_dropdown(language_frame, self.target_lang)

        # Play, Pause, Resume buttons
        playback_frame = tk.Frame(self.root)
        playback_frame.grid(row=2, column=0, columnspan=2, pady=10)

        self.play_button = self.create_button(playback_frame, "Play", self.play_audio)
        self.pause_button = self.create_button(playback_frame, "Pause", self.pause_audio)
        self.resume_button = self.create_button(playback_frame, "Resume", self.resume_audio)

        # Convert and Transcribe buttons
        action_frame = tk.Frame(self.root)
        action_frame.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.convert_input_to_speech_button = self.create_button(action_frame, "Convert Input to Speech", self.convert_input_to_speech)
        self.translate_button = self.create_button(action_frame, "Translate Text", self.translate_text)
        self.convert_output_to_speech_button = self.create_button(action_frame, "Convert Output to Speech", self.convert_output_to_speech)
        self.transcribe_button = self.create_button(action_frame, "Transcribe Speech", self.transcribe_speech)

    def create_label(self, parent, text):
        label = tk.Label(parent, text=text, font=("Arial", 12, "bold"))
        label.pack(pady=10)
        return label

    def create_text_area(self, parent):
        text_area = tk.Text(parent, height=10, width=50)
        text_area.pack()
        return text_area

    def create_language_dropdown(self, parent, variable):
        dropdown = tk.OptionMenu(parent, variable, *(language[0] for language in self.languages))
        dropdown.pack()
        return dropdown

    def create_button(self, parent, text, command):
        button = tk.Button(parent, text=text, font=("Arial", 12, "bold"), command=command)
        button.pack(side=tk.LEFT, padx=5)
        return button
    
    def translate_text(self):
        source_text = self.input_text.get("1.0", "end-1c")
        source_lang = self.get_language_code(self.source_lang.get())
        target_lang = self.get_language_code(self.target_lang.get())
        self.event_handler('translate_text', {'text': source_text, 'source_lang': source_lang, 'target_lang': target_lang})

    def transcribe_speech(self):
        audio_file_path = filedialog.askopenfilename()
        if not audio_file_path:
            return
        self.event_handler('transcribe_speech', {'audio_file': audio_file_path})

    def convert_input_to_speech(self):
        text = self.input_text.get("1.0", "end-1c")
        target_lang = self.get_language_code(self.target_lang.get())

        # Use the TextToSpeechModule to synthesize speech
        audio_data = self.text_to_speech_module.synthesize_speech(text, language_code=target_lang)

        self.audio_file_path = "input_speech.wav"
        with open(self.audio_file_path, "wb") as audio_file:
            audio_file.write(audio_data)

    def convert_output_to_speech(self):
        text = self.output_text.get("1.0", "end-1c")
        target_lang = self.get_language_code(self.target_lang.get())

        # Use the TextToSpeechModule to synthesize speech
        audio_data = self.text_to_speech_module.synthesize_speech(text, language_code=target_lang)

        self.audio_file_path = "output_speech.wav"
        with open(self.audio_file_path, "wb") as audio_file:
            audio_file.write(audio_data)

    def play_audio(self):
        if self.audio_file_path:
            pygame.mixer.music.load(self.audio_file_path)
            pygame.mixer.music.play()

    def pause_audio(self):
        pygame.mixer.music.pause()

    def resume_audio(self):
        pygame.mixer.music.unpause()

    def save_audio(self):
        if self.audio_file_path:
            dest = filedialog.asksaveasfilename(defaultextension=".wav", filetypes=[("WAV files", "*.wav")])
            if dest:
                os.rename(self.audio_file_path, dest)
                messagebox.showinfo("Save Audio", "Audio saved successfully.")
            else:
                messagebox.showwarning("Save Audio", "No destination selected. Audio not saved.")

    def display_translated_text(self, text):
        self.output_text.delete("1.0", "end")
        self.output_text.insert("1.0", text)

    def get_language_code(self, language):
        for lang, code in self.languages:
            if lang == language:
                return code
        return ""


    def display_error_message(self, message):
        messagebox.showerror("Error", message)

    def run(self):
        self.logger.info("GUI started")
        try:
            self.root.mainloop()
        finally:
            pygame.mixer.quit()

if __name__ == "__main__":
    gui = GuiModule(None)
    gui.run()