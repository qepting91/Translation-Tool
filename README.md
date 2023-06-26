# Translation Tool
 The Translation App is a graphical user interface (GUI) application that allows you to translate text, convert text to speech, and transcribe speech using various languages. It provides an intuitive interface for interacting with translation and speech synthesis functionality.
## Features

The Translation App offers the following features:

- Text translation: Enter text in the input text area, select the source language and target language from the dropdown menus, and click the "Translate Text" button to translate the text.

- Text-to-speech conversion:
  - Convert input text to speech: Enter text in the input text area, select the target language from the dropdown menu, and click the "Convert Input to Speech" button to generate speech audio from the input text.
  - Convert output text to speech: After translating text, the translated output will be displayed in the output text area. Select the target language from the dropdown menu and click the "Convert Output to Speech" button to generate speech audio from the translated text.

- Speech transcription: Click the "Transcribe Speech" button to transcribe speech from an audio file. The app will prompt you to select an audio file for transcription.

## Prerequisites

Before running the Translation App, ensure that you have the following dependencies installed:

- Python (version 3.7 or higher)
- Required Python packages: `pygame`, `google-cloud-texttospeech`, `google-cloud-speech`, `tkinter`

## Installation

1. Clone the repository to your local machine:

   git clone https://github.com/qepting91/translation-app.git

Install the required Python packages using pip:

pip install -r requirements.txt


## Setting Up Google Cloud Credentials
To use the Text-to-Speech and Speech-to-Text APIs in the Translation App, you'll need to set up Google Cloud credentials. Follow the steps below to create a Google Cloud project, enable the required APIs, and generate a service account key:

Create a Google Cloud project:

Go to the Google Cloud Console.
Click on the project dropdown and select "New Project".
Enter a name for your project and click "Create".
Enable the Text-to-Speech and Speech-to-Text APIs:

In the Google Cloud Console, navigate to the "APIs & Services" > "Library" section.
Search for "Text-to-Speech API" and "Speech-to-Text API".
Enable both APIs for your project.
Generate a service account key:

In the Google Cloud Console, navigate to the "APIs & Services" > "Credentials" section.

Click on the "Create credentials" dropdown and select "Service account key".

Fill in the required information for the service account.

Under "Key type", select "JSON" and click "Create".

Save the downloaded JSON key file in a secure location.

Set the GOOGLE_APPLICATION_CREDENTIALS environment variable:

Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the downloaded JSON key file.

This can be done using the command line or by setting the environment variable in your development environment.

Make sure to replace /path/to/keyfile.json with the actual path to the downloaded JSON key file.

Once you have completed these steps, your Google Cloud credentials will be set up and the Translation App will be able to authenticate and access the Text-to-Speech and Speech-to-Text APIs.

## Set the GOOGLE_APPLICATION_CREDENTIALS environment variable to the path of the JSON key file.

## Usage

To start the Translation App, navigate to the project directory and run the following command:

python main.py

The Translation App GUI will open, allowing you to interact with the translation and speech functionality.

Contributing
Contributions to the Translation App are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

License
The Translation App is released under the MIT License.


Feel free to customize and enhance the `README.md` file according to your project'
