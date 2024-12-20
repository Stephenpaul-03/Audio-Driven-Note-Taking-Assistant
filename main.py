import sys
import threading
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QTextEdit, QHBoxLayout
from PyQt5.QtCore import Qt, QThread, pyqtSignal
from PyQt5.QtGui import QColor
from modules.audio_recorder import start_recording, stop_recording
from modules.audio_transcriber import transcribe_audio
from modules.text_summarizer import summarize_text

class Worker(QThread):
    log_signal = pyqtSignal(str)

    def __init__(self, func, filename):
        super().__init__()
        self.func = func
        self.filename = filename

    def run(self):
        self.func(self.filename, log_func=self.emit_log)

    def emit_log(self, message):
        self.log_signal.emit(message)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Note Taking Assistant")
        self.setGeometry(100, 100, 300, 300)  
        self.setStyleSheet("background-color: #f0f0f0; font-family: Arial, sans-serif;")

        self.layout = QVBoxLayout()
        self.filename_label = QLabel("Enter Filename:")
        self.filename_label.setStyleSheet("font-weight: bold;")
        self.filename_input = QLineEdit()  
        self.filename_input.setPlaceholderText("e.g., recording_01.wav")
        self.filename_input.setStyleSheet("padding: 5px; border-radius: 5px;")
        
        self.log_label = QLabel("Log:")
        self.log_label.setStyleSheet("font-weight: bold;")
        self.log_text_edit = QTextEdit()  
        self.log_text_edit.setReadOnly(True)
        self.log_text_edit.setStyleSheet("background-color: #ffffff; border-radius: 5px; padding: 10px;")

        self.record_button = QPushButton("Start Recording")
        self.transcribe_button = QPushButton("Transcribe Audio")
        self.summarize_button = QPushButton("Summarize Text")

        self.record_button.setStyleSheet(self.get_button_style())
        self.transcribe_button.setStyleSheet(self.get_button_style())
        self.summarize_button.setStyleSheet(self.get_button_style())

        self.record_button.clicked.connect(self.toggle_recording)
        self.transcribe_button.clicked.connect(self.start_transcribing)
        self.summarize_button.clicked.connect(self.start_summarizing)

        self.layout.addWidget(self.filename_label)
        self.layout.addWidget(self.filename_input)
        self.layout.addWidget(self.log_label)
        self.layout.addWidget(self.log_text_edit)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.record_button)
        self.button_layout.addWidget(self.transcribe_button)
        self.button_layout.addWidget(self.summarize_button)
        self.button_layout.setSpacing(10)

        self.layout.addLayout(self.button_layout)
        self.layout.addStretch(1)  
        self.layout.addStretch(2)  

        self.setLayout(self.layout)

        self.is_recording = False  

    def get_button_style(self):
        return """
            QPushButton {
                background-color: #4CAF50;
                color: white;
                font-size: 14px;
                padding: 10px;
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #45a049;
            }
            QPushButton:pressed {
                background-color: #388e3c;
            }
        """

    def log_message(self, message):
        self.log_text_edit.append(message)
        self.log_text_edit.verticalScrollBar().setValue(self.log_text_edit.verticalScrollBar().maximum())

    def get_filename_from_user(self):
        return self.filename_input.text().strip()

    def toggle_recording(self):
        filename = self.get_filename_from_user() 
        if filename:
            if not self.is_recording:
                self.is_recording = True
                self.record_button.setText("Stop Recording")
                self.record_button.setStyleSheet(self.get_button_style().replace("#4CAF50", "#f44336"))  
                threading.Thread(target=self.record_audio_thread, args=(filename,), daemon=True).start()
            else:
                self.is_recording = False
                self.record_button.setText("Start Recording")
                self.record_button.setStyleSheet(self.get_button_style())  
                stop_recording(self.log_message, filename) 

    def record_audio_thread(self, filename):
        self.log_message("Recording started...")
        start_recording(filename, log_func=self.log_message) 
        self.log_message("Recording stopped.")

    def start_transcribing(self):
        filename = self.get_filename_from_user()
        if filename:
            self.log_text_edit.clear()
            self.worker = Worker(transcribe_audio, filename)
            self.worker.log_signal.connect(self.log_message)
            self.worker.start()

    def start_summarizing(self):
        filename = self.get_filename_from_user()
        if filename:
            self.log_text_edit.clear()
            self.worker = Worker(summarize_text, filename)
            self.worker.log_signal.connect(self.log_message)
            self.worker.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()  
    window.show()
    sys.exit(app.exec_())
