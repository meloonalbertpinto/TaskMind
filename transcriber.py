import os
import numpy as np
import wave
import tempfile
from sarvamai import SarvamAI

class Transcriber:
    def __init__(self, api_key=None):
        # Priority: Passed key -> Environment Variable
        self.api_key = api_key or os.getenv("SARVAM_API_KEY")
        if not self.api_key:
            raise ValueError("Sarvam API Key is required. Get one at dashboard.sarvam.ai")
        
        self.client = SarvamAI(api_subscription_key=self.api_key)

    def _numpy_to_wav(self, audio_data: np.ndarray, rate=16000):
        """Converts raw capture to temporary WAV for API transmission."""
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
        with wave.open(temp_file.name, 'wb') as wf:
            wf.setnchannels(1) 
            wf.setsampwidth(2) # 16-bit PCM
            wf.setframerate(rate)
            # Normalize and convert float32 to int16
            audio_int16 = (np.clip(audio_data, -1, 1) * 32767).astype(np.int16)
            wf.writeframes(audio_int16.tobytes())
        return temp_file.name

    def transcribe(self, audio_data: np.ndarray, language_code="unknown", rate=16000, mode="translate"):
        """
        Transcribes/Translates audio via Sarvam AI.
        language_code: 'hi-IN', 'kn-IN', 'en-IN', or 'unknown' for auto-detect.
        mode: 'transcribe' for same-language text, 'translate' for English output.
        """
        if audio_data.size == 0:
            return ""

        wav_path = self._numpy_to_wav(audio_data, rate=rate)
        try:
            with open(wav_path, "rb") as audio_file:
                response = self.client.speech_to_text.transcribe(
                    file=audio_file,
                    model="saaras:v3",
                    language_code=language_code,
                    mode=mode
                )
            return getattr(response, 'transcript', "")
        except Exception as e:
            print(f"Sarvam API Error: {e}")
            return ""
        finally:
            if os.path.exists(wav_path):
                os.remove(wav_path)

    def transcribe_file(self, file_path: str):
        """Directly transcribes .vtt or .wav files via Sarvam."""
        with open(file_path, "rb") as audio_file:
            response = self.client.speech_to_text.transcribe(
                file=audio_file,
                model="saaras:v3"
            )
        return response.get('transcript', "")