import google.generativeai as genai
import os
import json
from datetime import datetime

class Analyzer:
    def __init__(self, api_key=None):
        # Reverting to the user's verified Gemini API Key
        self.api_key = api_key or "AIzaSyACJPkCmspdQnmWXIQooiC6FmbMGcGB-84"
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = self._find_available_model()
        else:
            self.model = None
            print("Warning: GEMINI_API_KEY not found.")

    def _find_available_model(self):
        """Finds the best available Gemini model from the user's quota."""
        try:
            available_models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
            # Preference order: 1.5 Flash -> 1.5 Pro -> 1.0 Pro -> Any
            preferred = ['models/gemini-1.5-flash', 'models/gemini-1.5-pro', 'models/gemini-pro', 'models/gemini-flash-latest']
            
            for p in preferred:
                if p in available_models:
                    print(f"Using preferred model: {p}")
                    return genai.GenerativeModel(p)
            
            if available_models:
                print(f"No preferred model found. Using first available: {available_models[0]}")
                return genai.GenerativeModel(available_models[0])
            
            return None
        except Exception as e:
            print(f"Error listing models: {e}")
            return genai.GenerativeModel('gemini-1.5-flash') # Absolute fallback

    def analyze(self, transcript_list):
        if not self.model:
            return {"error": "Gemini API not configured"}
        
        if not transcript_list:
            return {"error": "No transcript content to analyze"}

        full_text = "\n".join(transcript_list)
        
        prompt = f"""Analyze the following meeting transcript and extract the information in JSON format:
        1. summary: A concise 2-3 sentence summary.
        2. key_points: A list of main topics.
        3. action_items: A list of tasks and next steps.
        4. key_decisions: A list of decisions made.

        Transcript:
        {full_text}

        Return ONLY the JSON object."""

        try:
            response = self.model.generate_content(prompt)
            
            # Check if there are candidates and if they have text
            if not response.candidates or not response.candidates[0].content.parts:
                return {"error": "AI response was empty (possibly blocked by safety filters). Please try rephrasing or adding more context."}
                
            text = response.text.strip()
            
            # Remove markdown formatting if present
            if text.startswith("```json"):
                text = text.split("```json")[1].split("```")[0].strip()
            elif text.startswith("```"):
                text = text.split("```")[1].split("```")[0].strip()
                
            analysis = json.loads(text)
            self.save_analysis(analysis, full_text)
            return analysis
        except Exception as e:
            error_str = str(e)
            print(f"Gemini analysis error: {error_str}")
            if "Safety" in error_str:
                 return {"error": "The content was flagged by Gemini's safety filters. Try clear and speak again."}
            return {"error": f"Gemini Error: {error_str}"}

    def ask_question(self, question, transcript_list):
        if not self.model:
            return {"error": "Gemini API not configured"}
        
        if not transcript_list:
            return {"error": "I need some transcription data before I can answer questions."}

        full_text = "\n".join(transcript_list)
        
        prompt = f"""You are a meeting assistant. Based ONLY on the transcript below, answer the user's question.
        If the user asks for "points", "key points", or a "list", provide a clear bulleted list with one item per line.
        
        If the answer is not in the transcript, say "I don't have enough information to answer that."

        Transcript:
        {full_text}

        User Question: {question}"""

        try:
            response = self.model.generate_content(prompt)
            
            if not response.candidates or not response.candidates[0].content.parts:
                return {"answer": "I'm sorry, I couldn't generate an answer for this. It might be blocked or contain no useful data."}

            return {"answer": response.text.strip()}
        except Exception as e:
            error_str = str(e)
            print(f"Gemini Q&A error: {error_str}")
            return {"error": f"Gemini Error: {error_str}"}

    def save_analysis(self, analysis, original_text):
        if not os.path.exists("sessions"):
            os.makedirs("sessions")
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"sessions/session_{timestamp}.json"
        
        data = {
            "timestamp": timestamp,
            "provider": "Google Gemini",
            "model": "gemini-2.0-flash",
            "analysis": analysis,
            "transcript": original_text
        }
        
        with open(filename, "w", encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return filename
