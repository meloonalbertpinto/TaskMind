# 🧠 TaskMind  
### AI Meeting-to-Action System for Engineering Teams

TaskMind is an AI-powered system that converts meeting discussions into structured engineering tasks. It helps teams transform meeting transcripts or audio recordings into summaries, decisions, and actionable tasks that can be pushed to tools like GitHub Issues.

---

## 🚀 Overview

Engineering meetings often include:

- technical discussions  
- feature planning  
- bug analysis  
- architectural decisions  
- task assignments  

Manually converting these conversations into development tasks can be slow and inefficient. TaskMind solves this by automatically extracting useful and actionable work items from meeting content.

---

## ✨ Key Features

- 📝 AI-generated meeting summaries  
- 💡 Extraction of key discussion points  
- ✅ Detection of decisions made during meetings  
- 📌 Action item / task extraction  
- 📄 Support for transcript input  
- 🎧 Support for audio input with speech-to-text  
- 🔗 Integration with GitHub Issues  

---

## 🛠️ Tech Stack

**Frontend**
- HTML  
- Tailwind CSS  
- JavaScript  

**Backend**
- FastAPI  
- Python  

**AI Layer**
- Llama 3.1  

**Speech-to-Text**
- Sarvam API  
- Whisper / faster-whisper  

**Database**
- SQLite  

---

## 🏗️ Architecture

```text
User Interface
     ↓
FastAPI Backend
     ↓
AI Processing Layer
     ↓
Speech-to-Text Layer
     ↓
SQLite Database
     ↓
GitHub / Jira Integrations
```

---

## ⚙️ Main API Endpoints

- `POST /analyze-transcript`
- `POST /analyze-audio`
- `POST /integrations/github/push`
- `GET /meetings`
- `GET /health`

---

## 🔄 Workflow

1. User uploads or pastes meeting content  
2. Audio is converted to text if needed  
3. AI analyzes the transcript  
4. System generates:
   - summary
   - decisions
   - action items  
5. User reviews tasks  
6. Tasks can be pushed to GitHub Issues  

---

## 📌 Future Enhancements

- 🎯 Priority detection  
- 👤 Suggested assignee extraction  
- ⏰ Deadline detection  
- 📤 Export reports  
- 🔔 Slack notifications  

---

## 👨‍💻 Author

Developed as a prototype to demonstrate how AI can transform engineering meeting discussions into structured development tasks.
