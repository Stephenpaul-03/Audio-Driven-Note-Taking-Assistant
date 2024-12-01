# VoxNote

## Description

VoxNote is a Python-based application designed to record audio, transcribe it into text, and summarize the transcriptions. The application features a user-friendly interface built with PyQt5, making it accessible for users looking for an efficient audio processing tool.

## Note

VoxNote requires FFmpeg to convert, stream, and manipulate audio files that are recorded. FFmpeg is a powerful open-source tool that helps process audio and video files, and it is an essential component of this project to ensure smooth audio handling and transcription.

Please follow the steps below to install and configure FFmpeg on your system.

#### 1. **Download FFmpeg**

   - Go to the [FFmpeg official website](https://ffmpeg.org/download.html).
   - Select the Package based on your Operating System.
   - Download the latest version (e.g., `ffmpeg-release-essentials.zip`).

#### 2. **Extract FFmpeg**

   - Once downloaded, extract the zip file to a location on your computer. 
     - Example: `C:\ffmpeg\`
   - Inside the extracted folder, you should see a folder named `bin` containing the `ffmpeg.exe` file.

#### 3. **Add FFmpeg to System PATH**

   To make sure FFmpeg is available in your command line or any subprocess call (like Whisper), add its `bin` directory to your system's `PATH` environment variable:

### On Windows:
   1. Right-click **This PC** (or **My Computer**) and select **Properties**.
   2. Click **Advanced system settings** on the left, then click **Environment Variables**.
   3. Under **System variables**, scroll to find `Path` and select **Edit**.
   4. In the edit window, click **New** and add the path to the `bin` directory of your FFmpeg folder. Example: `C:\ffmpeg\bin\`.
   5. Click **OK** to save the changes.

### On macOS and Linux:
   1. Open the terminal.
   2. Run the following command to open the `.bash_profile` or `.zshrc` file:
      ```bash
      nano ~/.bash_profile   # For bash users
      nano ~/.zshrc           # For zsh users (default on macOS Catalina and above)
      ```
   3. Add the following line to the file:
      ```bash
      export PATH=$PATH:/path/to/ffmpeg/bin
      ```
   4. Save the file and close the editor.
   5. Reload the profile:
      ```bash
      source ~/.bash_profile   # For bash users
      source ~/.zshrc           # For zsh users
      ```

#### 4. **Verify FFmpeg Installation**

   - Open a terminal (Command Prompt on Windows or Terminal on macOS/Linux).
   - Type the following command to verify FFmpeg is installed:
     ```bash
     ffmpeg -version
     ```
   - You should see output showing FFmpeg’s version and configuration details.

#### 5. **Run Your Application**

   Once FFmpeg is installed and configured correctly, you can run your application.

## Features

- **Audio Recording**: Start and stop audio recordings easily.
- **Audio Transcription**: Convert recorded audio files into text using speech recognition.
- **Text Summarization**: Summarize the transcriptions for quick insights.

## Project Structure

```
VoxNote/
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

To set up the VoxNote on your local machine, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/Stephenpaul-03/VoxNote.git
```

2. Navigate to Project Directory:
```bash
cd VoxNote
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