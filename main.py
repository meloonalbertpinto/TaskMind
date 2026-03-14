import time
import collections
import numpy as np
from audio_capture import AudioCapture
from transcriber import Transcriber

def run_realtime_transcription():
    # Replace with your actual key
    API_KEY = "sk_hfjvmsx8_Ipo6I5KpHfj5jinozgwWC6aa"
    
    print("--- Initializing Sarvam AI Multilingual System ---")
    recorder = AudioCapture()
    model = Transcriber(api_key=API_KEY)
    
    # Stores audio for context
    context_buffer = collections.deque(maxlen=2) 

    try:
        recorder.start()
        print("--- LISTENING (Supports Hindi, Kannada, etc.) ---")

        while True:
            # Capture 10s chunks
            audio_chunk = recorder.get_chunk(duration=10)
            
            if audio_chunk.size > 0:
                context_buffer.append(audio_chunk)
                combined_audio = np.concatenate(list(context_buffer))
                
                # Use 'hi-IN' for Hindi, 'en-IN' for English, or 'unknown' for Auto
                text = model.transcribe(combined_audio, language_code="en-IN", rate=recorder.rate)
                
                if text.strip():
                    print(f"Transcript: {text}")
            
            time.sleep(0.1)

    except KeyboardInterrupt:
        recorder.force_stop() # Use our safety method on exit
    finally:
        recorder.stop()

if __name__ == "__main__":
    run_realtime_transcription()