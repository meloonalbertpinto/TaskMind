import numpy as np
import pyaudiowpatch as pyaudio
import datetime

class AudioCapture:
    def __init__(self, rate=16000, chunk_size=1024):
        self.rate = rate
        self.chunk_size = chunk_size
        self.p = pyaudio.PyAudio()
        self.stream = None
        self.is_recording = False
        self.full_session_buffer = [] 

    def _get_loopback_device(self):
        """Manually finds the WASAPI loopback device."""
        try:
            wasapi_info = None
            for i in range(self.p.get_host_api_count()):
                api_info = self.p.get_host_api_info_by_index(i)
                if "WASAPI" in api_info.get('name'):
                    wasapi_info = api_info
                    break
            
            if not wasapi_info:
                return self.p.get_default_input_device_info()

            for i in range(self.p.get_device_count()):
                dev_info = self.p.get_device_info_by_index(i)
                if dev_info.get('hostApi') == wasapi_info.get('index') and dev_info.get('isLoopbackDevice'):
                    return dev_info
            
            return self.p.get_default_output_device_info()
        except Exception:
            return self.p.get_default_input_device_info()

    def start(self):
        device = self._get_loopback_device()
        self.is_recording = True
        self.rate = int(device['defaultSampleRate'])
        self.channels = device['maxInputChannels']
        self.stream = self.p.open(
            format=pyaudio.paFloat32,
            channels=self.channels,
            rate=self.rate,
            input=True,
            frames_per_buffer=self.chunk_size,
            input_device_index=device['index']
        )
        print(f"Captured device found: {device['name']}")

    def get_chunk(self, duration=5):
        if not self.is_recording: return np.array([])
        num_chunks = int(self.rate / self.chunk_size * duration)
        chunks = []
        for _ in range(num_chunks):
            if not self.is_recording: break
            try:
                data = self.stream.read(self.chunk_size, exception_on_overflow=False)
                numpy_data = np.frombuffer(data, dtype=np.float32)
                if self.channels > 1:
                    numpy_data = numpy_data.reshape(-1, self.channels).mean(axis=1)
                chunks.append(numpy_data)
                self.full_session_buffer.append(numpy_data)
            except Exception:
                chunks.append(np.zeros(self.chunk_size, dtype=np.float32))
        return np.concatenate(chunks) if chunks else np.array([])

    def force_stop(self):
        print("\n[!] KILL BOT ACTIVATED")
        self.is_recording = False
        if self.full_session_buffer:
            final_audio = np.concatenate(self.full_session_buffer)
            filename = f"emergency_{datetime.datetime.now().strftime('%H%M%S')}.npy"
            np.save(filename, final_audio)
        self.stop()

    def stop(self):
        self.is_recording = False
        if self.stream:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()