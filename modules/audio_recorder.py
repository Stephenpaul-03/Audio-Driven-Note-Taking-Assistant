import os
import sounddevice as sd
import numpy as np
import wave

SAMPLE_RATE = 16000  
CHANNELS = 1         
audio_data = []

def find_audio_device(device_name):
    devices = sd.query_devices()
    for idx, device in enumerate(devices):
        if device_name in device['name'] and device['max_input_channels'] > 0:
            return idx
    return None

def start_recording(filename, log_func):
    global audio_data  
    audio_data = []
    
    device_index = find_audio_device("Stereo Mix")
    if device_index is None:
        log_func("Stereo Mix not found, trying to find an available audio device.")
        device_index = find_audio_device("Virtual Cable")  

    if device_index is None:
        log_func("No appropriate audio input device found.")
        return

    with sd.InputStream(samplerate=SAMPLE_RATE, channels=CHANNELS, dtype='int16', device=device_index) as stream:
        try:
            while True:  
                data = stream.read(SAMPLE_RATE)[0]
                audio_data.append(data)
        except Exception as e:
            log_func(f"Error during recording: {str(e)}")

def stop_recording(log_func, filename):
    if not audio_data:
        log_func("No audio data to save.")
        return

    log_func("Stopping recording.")
    audio_file_path = os.path.join(os.path.dirname(__file__),"..","Files","Recordings",f"{filename}.wav")
    os.makedirs(os.path.dirname(audio_file_path), exist_ok=True)
    save_audio_to_wav(audio_file_path, np.concatenate(audio_data), SAMPLE_RATE)
    log_func(f"Audio saved.")

def save_audio_to_wav(filename, audio_data, sample_rate):
    with wave.open(filename, 'wb') as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(2) 
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

if __name__ == "__main__":
    filename = input()
    start_recording(filename)
