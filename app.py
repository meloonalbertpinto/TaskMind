from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager
import asyncio
import collections
import numpy as np
import threading
import os
import time
from audio_capture import AudioCapture
from transcriber import Transcriber
from analyzer import Analyzer

API_KEY = "sk_hfjvmsx8_Ipo6I5KpHfj5jinozgwWC6aa"

class TranscriptionManager:
    def __init__(self):
        self.active = False
        self.transcripts = []
        self.clients = set()
        self.loop_thread = None
        self.main_loop = None
        self.target_language = "unknown"
        self.mode = "translate"
        self.full_transcript_history = []
        self.analyzer = Analyzer()
        self._lock = threading.Lock()

    async def register_client(self, websocket: WebSocket):
        await websocket.accept()
        self.clients.add(websocket)
        # Send existing transcripts
        for t in self.transcripts:
            try:
                await websocket.send_text(t)
            except:
                pass

    def unregister_client(self, websocket: WebSocket):
        if websocket in self.clients:
            self.clients.remove(websocket)

    async def broadcast(self, message: str):
        if not message or not message.strip():
            return
            
        self.transcripts.append(message)
        self.full_transcript_history.append(message)
        
        if len(self.transcripts) > 100:
            self.transcripts.pop(0)
        
        disconnected_clients = []
        for client in self.clients:
            try:
                await client.send_text(message)
            except Exception:
                disconnected_clients.append(client)
        
        for client in disconnected_clients:
            self.unregister_client(client)

    def start_transcription(self, language_code="unknown", mode="translate"):
        with self._lock:
            self.target_language = language_code
            self.mode = mode
            
            if self.active:
                print(f"Update settings: {language_code}, {mode}")
                return
            
            # If a thread exists but active is False, wait for it to join
            if self.loop_thread and self.loop_thread.is_alive():
                print("Waiting for previous session to clean up...")
                self.loop_thread.join(timeout=5)

            print("Starting new transcription session...")
            self.active = True
            self.loop_thread = threading.Thread(target=self._run_loop, daemon=True)
            self.loop_thread.start()

    def stop_transcription(self):
        with self._lock:
            if not self.active:
                return
            print("Stopping transcription session...")
            self.active = False
            # The thread will clean up itself and the recorder

    def clear_history(self):
        with self._lock:
            self.transcripts = []
            self.full_transcript_history = []

    def get_analysis(self):
        return self.analyzer.analyze(self.full_transcript_history)

    def _run_loop(self):
        # We create the recorder INSIDE the thread to ensure it's fresh
        recorder = None
        model = None
        try:
            recorder = AudioCapture()
            model = Transcriber(api_key=API_KEY)
            recorder.start()
            
            context_buffer = collections.deque(maxlen=2)
            
            while self.active:
                # Use short duration for responsiveness check
                audio_chunk = recorder.get_chunk(duration=3) 
                
                # Check active again after chunk fetch
                if not self.active:
                    break
                    
                if audio_chunk.size > 0:
                    context_buffer.append(audio_chunk)
                    combined_audio = np.concatenate(list(context_buffer))
                    
                    # Capture current settings
                    with self._lock:
                        lang = self.target_language
                        mode = self.mode
                    
                    text = model.transcribe(combined_audio, language_code=lang, rate=recorder.rate, mode=mode)
                    
                    if text.strip() and self.main_loop:
                        asyncio.run_coroutine_threadsafe(self.broadcast(text), self.main_loop)
                
                time.sleep(0.1)
        except Exception as e:
            print(f"CRITICAL ERROR in transcription loop: {e}")
            import traceback
            traceback.print_exc()
        finally:
            self.active = False
            if recorder:
                try:
                    print("Cleaning up recorder...")
                    recorder.stop()
                except Exception as e:
                    print(f"Error terminating recorder: {e}")
            print("Transcription thread completely finished.")

manager = TranscriptionManager()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    manager.main_loop = asyncio.get_running_loop()
    yield
    # Shutdown logic
    manager.stop_transcription()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/start")
async def start(config: dict = None):
    lang = config.get("language", "unknown") if config else "unknown"
    mode = config.get("mode", "translate") if config else "translate"
    manager.start_transcription(language_code=lang, mode=mode)
    return {"status": "started"}

@app.post("/stop")
async def stop():
    manager.stop_transcription()
    return {"status": "stopped"}

@app.post("/analyze")
async def analyze():
    try:
        analysis = manager.get_analysis()
        return analysis
    except Exception as e:
        print(f"Error in /analyze endpoint: {e}")
        return {"error": str(e)}

@app.post("/ask")
async def ask(payload: dict):
    question = payload.get("question")
    if not question:
        return {"error": "Question is required"}
    
    try:
        answer = manager.analyzer.ask_question(question, manager.full_transcript_history)
        return answer
    except Exception as e:
        print(f"Error in /ask endpoint: {e}")
        return {"error": str(e)}

@app.post("/clear")
async def clear():
    manager.clear_history()
    return {"status": "cleared"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.register_client(websocket)
    try:
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.unregister_client(websocket)

# Serve the static frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def get_index():
    return FileResponse(os.path.join("static", "index.html"))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
