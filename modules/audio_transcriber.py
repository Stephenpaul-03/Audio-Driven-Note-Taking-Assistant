import os
import whisper

def transcribe_audio(filename, log_func):
    audio_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..","Files","Recordings")
    audio_file_path = os.path.join(audio_folder, f"{filename}.wav")
    
    transcription_folder = os.path.join(audio_folder, "..","Transcripts")
    os.makedirs(transcription_folder, exist_ok=True) 
    transcription_file_path = os.path.join(transcription_folder, f"{filename}.txt")

    if os.path.exists(audio_file_path):
        model = whisper.load_model("tiny.en")
        log_func(f"Transcribing audio")
        result = model.transcribe(audio_file_path)
        with open(transcription_file_path, "w") as f:
            f.write(result['text'])
        log_func(f"Transcription saved")
    else:
        log_func(f"No audio file found. Please ensure the filename is correct.")
