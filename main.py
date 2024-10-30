import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QTextEdit
from modules.audio_recorder import start_recording, stop_recording
from modules.audio_transcriber import transcribe_audio
from modules.text_summarizer import summarize_text

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hermes Audio Assistant")
        self.setGeometry(100, 100, 400, 600)

        self.layout = QVBoxLayout()

        self.filename_label = QLabel("Filename:")
        self.filename_input = QLineEdit()  
        self.log_label = QLabel("Log:")
        self.log_text_edit = QTextEdit()  
        self.log_text_edit.setReadOnly(True)

        self.record_button = QPushButton("Start Recording")
        self.transcribe_button = QPushButton("Transcribe")
        self.summarize_button = QPushButton("Summarize")

        self.record_button.clicked.connect(self.toggle_recording)
        self.transcribe_button.clicked.connect(self.start_transcribing)
        self.summarize_button.clicked.connect(self.start_summarizing)

        self.layout.addWidget(self.filename_label)
        self.layout.addWidget(self.filename_input)
        self.layout.addWidget(self.log_label)
        self.layout.addWidget(self.log_text_edit)
        self.layout.addWidget(self.record_button)
        self.layout.addWidget(self.transcribe_button)
        self.layout.addWidget(self.summarize_button)

        self.setLayout(self.layout)

        self.is_recording = False  

    def log_message(self, message):
        print(message)  
        self.log_text_edit.append(message)

    def get_filename_from_user(self):
        return self.filename_input.text().strip()

    def toggle_recording(self):
        filename = self.get_filename_from_user() 
        if filename:
            if not self.is_recording:
                self.is_recording = True
                self.record_button.setText("Stop Recording")
                threading.Thread(target=self.record_audio_thread, args=(filename,), daemon=True).start()
            else:
                self.is_recording = False
                self.record_button.setText("Start Recording")
                stop_recording(self.log_message, filename) 

    def record_audio_thread(self, filename):
        self.log_message("Recording started.")
        start_recording(filename, log_func=self.log_message) 
        self.log_message("Recording stopped.")

    def start_transcribing(self):
        filename = self.get_filename_from_user()
        if filename:
            self.log_text_edit.clear()
            threading.Thread(target=self.transcribe_audio_thread, args=(filename,), daemon=True).start()

    def transcribe_audio_thread(self, filename):
        self.log_message("Transcription started.")
        transcribe_audio(filename, log_func=self.log_message)
        self.log_message("Transcription completed.")

    def start_summarizing(self):
        filename = self.get_filename_from_user()
        if filename:
            self.log_text_edit.clear()
            threading.Thread(target=self.summarize_audio_thread, args=(filename,), daemon=True).start()

    def summarize_audio_thread(self, filename):
        self.log_message("Summarization started.")
        summarize_text(filename, log_func=self.log_message)
        self.log_message("Summarization completed.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec_())
