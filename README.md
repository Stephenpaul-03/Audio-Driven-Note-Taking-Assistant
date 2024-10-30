# Hermes

## Description

Hermes is a Python-based application designed to record audio, transcribe it into text, and summarize the transcriptions. The application features a user-friendly interface built with PyQt5, making it accessible for users looking for an efficient audio processing tool.

## Features

- **Audio Recording**: Start and stop audio recordings easily.
- **Audio Transcription**: Convert recorded audio files into text using speech recognition.
- **Text Summarization**: Summarize the transcriptions for quick insights.

## Project Structure

```
Hermes/
├── main.py                     # Main application file
├── requirements.txt            # Dependencies required for the project
├── LICENSE                     # MIT License
├── README.md                   # README File
├── models/                     # Contains machine learning models
│   ├── distilBART              # Model for text summarization
│   └── whisper-tiny.en         # Model for speech recognition
└── modules/                    # Contains module files for different functionalities
    ├── audio_recorder.py       # Handles audio recording functionality
    ├── audio_transcriber.py    # Handles audio transcription functionality
    └── text_summarizer.py      # Handles text summarization functionality
```

## Installation

To set up the Hermes on your local machine, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/Stephenpaul-03/Hermes.git
```

2. Navigate to Project Directory:
```bash
cd Hermes
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

## Usage

1. **Start Recording**: Enter a filename in the input field and click "Start Recording." Click again to stop recording.
2. **Transcribe Audio**: Enter the filename of the recorded audio and click "Transcribe."
3. **Summarize Text**: Enter the filename of the transcription and click "Summarize."


## Code Overview

* **main.py**: The main entry point of the application that initializes the GUI, handles user interactions, and manages audio recording, transcription, and summarization processes.
* **modules/audio_recorder.py**: Contains functions for recording audio, including starting and stopping the recording, as well as logging messages related to the recording process.
* **modules/audio_transcriber.py**: Implements functionality to transcribe recorded audio files into text using a speech recognition model, with logging support for tracking the progress.
* **modules/text_summarizer.py**: Contains functions for summarizing transcribed text using a text summarization model, allowing users to generate concise summaries from longer transcripts.
* **models/distilBART**: A pre-trained model for text summarization, utilized to generate summaries of the transcriptions which is downloaded to your local device on the first use.
* **models/whisper tiny.en**: A speech recognition model used to transcribe audio files into text which is downloaded to your local device on the first use.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
* **DistilBART**: Developed by the Hugging Face team, this model is a distilled version of BART (Bidirectional and Auto-Regressive Transformers) that provides efficient text summarization capabilities.
* **Whisper**: Created by OpenAI, Whisper is a powerful speech recognition model that enables accurate transcription of audio to text in various languages and accents.