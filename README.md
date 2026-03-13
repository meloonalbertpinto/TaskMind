# TaskMind
AI Meeting-to-Action System for Engineering Teams  TaskMind is an AI-powered system that transforms meeting discussions into structured engineering tasks.


🧠 TaskMind
AI Meeting-to-Action System for Engineering Teams

TaskMind is an AI-powered system that transforms meeting discussions into structured engineering tasks.

Instead of manually writing meeting notes and creating tickets, TaskMind automatically analyzes meeting transcripts or audio recordings to generate summaries, decisions, and actionable tasks that can be pushed directly to workflow tools like GitHub Issues.

🚀 Project Overview

Engineering meetings often include:

technical discussions

feature planning

bug analysis

architectural decisions

task assignments

However, converting these conversations into clear and actionable development tasks is often time-consuming.

TaskMind solves this problem by using AI to automatically extract structured action items from meeting discussions.

✨ Key Features
🧠 AI Meeting Analysis

TaskMind uses AI models to automatically analyze meeting content and generate:

📝 Meeting Summary

💡 Key Discussion Points

✅ Decisions Taken

📌 Action Items / Tasks

These tasks are structured so they can easily be converted into engineering tickets.

🎤 Multiple Meeting Input Options

TaskMind supports several input formats:

📄 Paste meeting transcript

📂 Upload transcript files (.txt / .vtt / .srt)

🎧 Upload meeting audio recordings

🎙 Optional live microphone recording (future feature)

🔊 Speech-to-Text Processing

For audio meetings, TaskMind converts speech into text using:

Sarvam API

Whisper / faster-whisper

Local speech-to-text models

After transcription, the AI analyzes the meeting content.

📊 Structured Output

After analysis, TaskMind presents results in a structured format:

Meeting transcript viewer

AI-generated summary

Key decisions section

Action items table

Each action item can later be pushed to external workflow tools.

🔗 Workflow Integration

TaskMind integrates with engineering tools to create real development tasks.

Supported integrations:

🐙 GitHub Issues (primary integration)

🧰 Jira Cloud (optional)

📋 Trello / Linear (future scope)

Users can review tasks and push them directly as GitHub Issues.

🖥 User Interface

The system provides a simple and clean web interface including:

📥 Meeting Input Panel

📜 Transcript Viewer

📑 Summary Section

💡 Decisions Section

📋 Action Items Table

🔗 Push-to-GitHub Button

📊 Task Push History

🧱 Technology Stack
Frontend

HTML

Tailwind CSS

Vanilla JavaScript

Lightweight UI designed for simplicity and fast prototyping.

Backend

FastAPI

Python

Handles:

API endpoints

AI orchestration

integrations with external tools

AI Processing Layer

TaskMind uses Llama 3.1 (local LLM) to perform:

meeting summarization

decision extraction

action item detection

task structuring

Speech-to-Text Layer

Supported speech processing tools:

Sarvam API

Whisper / faster-whisper

Local STT models

🏗 System Architecture
User Interface (HTML + Tailwind)
        │
        ▼
FastAPI Backend
        │
        ├── Transcript Processing
        │
        ├── AI Processing Layer
        │      ├ Summary Generator
        │      ├ Decision Extractor
        │      ├ Action Item Extractor
        │      └ Task Structurer
        │
        ├── Speech-to-Text Layer
        │      ├ Sarvam API
        │      └ Whisper
        │
        ├── SQLite Database
        │
        └── Integrations
               ├ GitHub Issues API
               ├ Jira Cloud API (optional)
               └ Slack Webhooks (future)
⚙️ Backend API Endpoints

Example API endpoints used in TaskMind:

POST /analyze-transcript
POST /analyze-audio
POST /integrations/github/push
POST /integrations/jira/push
GET  /meetings
GET  /meetings/{id}
GET  /health
🔄 System Workflow
Option 1 — Transcript Input
User pastes meeting transcript
        ↓
Backend sends transcript to AI model
        ↓
AI generates summary, decisions, and tasks
        ↓
Results displayed in UI
        ↓
User reviews tasks
        ↓
Tasks pushed to GitHub Issues
Option 2 — Audio Input
User uploads meeting audio
        ↓
Speech-to-text converts audio to transcript
        ↓
AI analyzes transcript
        ↓
Summary + decisions + action items generated
        ↓
Tasks pushed to GitHub Issues
🌟 Advanced Features (Future Enhancements)

Planned intelligent capabilities include:

🎯 Priority detection (High / Medium / Low)

👤 Suggested task assignee extraction

⏰ Deadline detection

📊 Confidence score for extracted tasks

✏ Editable task cards before pushing

🔍 Search previous meetings

📤 Export meeting reports (JSON / Markdown)

🔔 Slack webhook notifications

📊 Smart Meeting Insights (Future)

TaskMind may also generate meeting analytics such as:

📈 Meeting Health Score

Number of decisions made

Unresolved blockers

Tasks without owners


can u create me a simple read me formar for thie contents in a single file format.
Below is a ready-to-paste **README.md** that includes:

- setup
- terminal commands
- folder creation
- install steps
- how to run backend/frontend
- how to run Ollama
- how to test
- common checks
- troubleshooting

You can copy this directly into your project.

---

# README.md

md
# AI Meeting-to-Action System

An AI-powered prototype for engineering teams that converts meeting transcripts into:

- concise summaries
- key discussion points
- decisions
- structured action items
- GitHub Issues

This project uses:

- **FastAPI** for backend
- **HTML + Tailwind CSS + JavaScript** for frontend
- **Llama 3.1 via Ollama** for local LLM analysis
- **SQLite** for storage
- **GitHub Issues API** for workflow integration

---

# 1. Features

## Current MVP
- Paste meeting transcript
- Analyze transcript using Llama 3.1
- Extract:
  - summary
  - key discussion points
  - decisions
  - action items
- Push extracted tasks to GitHub Issues
- Clean dark theme UI

## Planned Extensions
- audio upload
- speech-to-text
- live mic recording
- Jira integration
- meeting history
- export JSON / Markdown

---

# 2. Project Structure
bash
ai-meeting-to-action/
│
├── backend/
│   ├── app/
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── prompts.py
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── llm_service.py
│   │   │   └── github_service.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── analyze.py
│   │       └── integrations.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   └── app.js
│
└── README.md
---

# 3. Prerequisites

Before running this project, make sure you have:

- **Python 3.10+**
- **Ollama installed**
- **Git**
- Internet access for GitHub API calls
- A GitHub repository for issue creation

---

# 4. Create Project Folder

Open terminal and run:
bash
mkdir ai-meeting-to-action
cd ai-meeting-to-action
Create required folders:
bash
mkdir backend
mkdir frontend
mkdir backend/app
mkdir backend/app/routes
mkdir backend/app/services
Create required empty files:

### On Windows PowerShell
powershell
New-Item backend/app/routes/__init__.py -ItemType File
New-Item backend/app/services/__init__.py -ItemType File
New-Item backend/app/main.py -ItemType File
New-Item backend/app/database.py -ItemType File
New-Item backend/app/models.py -ItemType File
New-Item backend/app/schemas.py -ItemType File
New-Item backend/app/prompts.py -ItemType File
New-Item backend/app/routes/analyze.py -ItemType File
New-Item backend/app/routes/integrations.py -ItemType File
New-Item backend/app/services/llm_service.py -ItemType File
New-Item backend/app/services/github_service.py -ItemType File
New-Item backend/requirements.txt -ItemType File
New-Item frontend/index.html -ItemType File
New-Item frontend/app.js -ItemType File
New-Item README.md -ItemType File
### On Mac/Linux
bash
touch backend/app/routes/__init__.py
touch backend/app/services/__init__.py
touch backend/app/main.py
touch backend/app/database.py
touch backend/app/models.py
touch backend/app/schemas.py
touch backend/app/prompts.py
touch backend/app/routes/analyze.py
touch backend/app/routes/integrations.py
touch backend/app/services/llm_service.py
touch backend/app/services/github_service.py
touch backend/requirements.txt
touch frontend/index.html
touch frontend/app.js
touch README.md
Now paste the project code into the respective files.

---

# 5. Create Python Virtual Environment

From the project root:

## Windows
bash
python -m venv venv
venv\Scripts\activate
## Mac/Linux
bash
python3 -m venv venv
source venv/bin/activate
When activated, your terminal should show `(venv)`.

---

# 6. Install Backend Dependencies

Run:
bash
pip install -r backend/requirements.txt
If you want to install manually:
bash
pip install fastapi uvicorn sqlalchemy python-dotenv requests python-multipart pydantic
To confirm installation:
bash
pip list
You should see packages like:
- fastapi
- uvicorn
- sqlalchemy
- requests

---

# 7. Install and Run Ollama

## Check if Ollama is installed
bash
ollama --version
If Ollama is not installed, install it from:
bash
https://ollama.com/download
## Pull Llama 3.1
bash
ollama pull llama3.1
## Run Llama 3.1
bash
ollama run llama3.1
This starts the model locally.

### Important
Keep Ollama installed and available locally.  
The FastAPI backend will call Ollama on:
bash
http://localhost:11434
## Check Ollama server
Open another terminal and run:
bash
curl http://localhost:11434/api/tags
If working, it should return model information.

If `curl` is not available, open browser:
bash
http://localhost:11434
or just continue and test using backend.

---

# 8. Run Backend

Open a new terminal.

Go to project root:
bash
cd ai-meeting-to-action
Activate virtual environment again if needed.

## Option A: Run from project root
bash
uvicorn backend.app.main:app --reload
## Option B: If import error happens, run from backend folder
bash
cd backend
uvicorn app.main:app --reload
### Expected output
You should see something like:
bash
INFO:     Uvicorn running on http://127.0.0.1:8000
---

# 9. Check Backend Health

Open browser and visit:
bash
http://127.0.0.1:8000
You should see:
json
{"message":"AI Meeting-to-Action Backend Running"}
Also test Swagger docs:
bash
http://127.0.0.1:8000/docs
If `/docs` opens, backend is working correctly.

---

# 10. Run Frontend

Open another terminal.

Go to frontend folder:
bash
cd ai-meeting-to-action/frontend
Run a local static server:

## Using Python
bash
python -m http.server 5500
Then open in browser:
bash
http://127.0.0.1:5500
You should see the dark UI page.

---

# 11. Correct Run Order

Always run the app in this order:

## Terminal 1 — Ollama
bash
ollama run llama3.1
## Terminal 2 — Backend
From project root:
bash
uvicorn backend.app.main:app --reload
or from backend folder:
bash
cd backend
uvicorn app.main:app --reload
## Terminal 3 — Frontend
bash
cd frontend
python -m http.server 5500
Then open:
bash
http://127.0.0.1:5500
---

# 12. How to Test the App

Paste this sample transcript into the UI:
text
In today’s sprint planning meeting, the team discussed a login issue that must be fixed before the next release. The backend team will investigate the authentication bug and deploy a fix by Friday. We also agreed that the API needs rate limiting to prevent abuse, and this should be added in the next sprint. The UI team will redesign the dashboard analytics widget to improve readability. The product manager asked for a review of the notification settings flow, but no immediate action was assigned.
Set title:
text
Sprint Planning - Week 12
Click:
text
Analyze Meeting
Expected result:
- summary generated
- key discussion points listed
- decisions listed
- action items extracted

---

# 13. GitHub Integration Setup

To push tasks to GitHub Issues, create a GitHub Personal Access Token.

## Steps
1. Open GitHub
2. Go to **Settings**
3. Go to **Developer Settings**
4. Open **Personal Access Tokens**
5. Create token with repository issue permissions

For classic token:
- `repo`

For fine-grained token:
- Issues: Read and Write
- Repository access to your target repo

## In UI enter:
- Repo Owner
- Repo Name
- GitHub Token

Then click:
text
Push All Tasks to GitHub Issues
If successful, issue links will appear in the UI.

---

# 14. Terminal Commands Summary

## Create and enter project
bash
mkdir ai-meeting-to-action
cd ai-meeting-to-action
## Create virtual environment
### Windows
bash
python -m venv venv
venv\Scripts\activate
### Mac/Linux
bash
python3 -m venv venv
source venv/bin/activate
## Install dependencies
bash
pip install -r backend/requirements.txt
## Pull Llama model
bash
ollama pull llama3.1
## Run Llama locally
bash
ollama run llama3.1
## Run backend
bash
uvicorn backend.app.main:app --reload
## Alternative backend run
bash
cd backend
uvicorn app.main:app --reload
## Run frontend
bash
cd frontend
python -m http.server 5500
---

# 15. What to Check at Each Step

## After creating virtual environment
Check:
bash
python --version
## After installing dependencies
Check:
bash
pip list
## After pulling Ollama model
Check:
bash
ollama list
You should see:
bash
llama3.1
## After running backend
Check browser:
bash
http://127.0.0.1:8000
## After running frontend
Check browser:
bash
http://127.0.0.1:5500
## After clicking Analyze
Check backend terminal for any errors.

---

# 16. Common Troubleshooting

## Problem: `ModuleNotFoundError`
### Fix
Run backend from correct location:
bash
cd backend
uvicorn app.main:app --reload
---

## Problem: Ollama connection refused
### Fix
Make sure Ollama is running:
bash
ollama run llama3.1
Also verify:
bash
ollama list
---

## Problem: JSON parsing fails from LLM
### Cause
The model may return extra text around JSON.

### Fix
- keep transcript shorter
- retry once
- ensure prompt file is correctly pasted

---

## Problem: Frontend opens but analyze fails
### Check
- backend is running on port 8000
- frontend is running on port 5500
- browser console for errors
- backend terminal logs

---

## Problem: GitHub issue push fails
### Check
- token permissions
- repo owner name
- repo name
- repository exists
- token has issue creation rights

---

## Problem: Port already in use
### Fix
Use another port.

For frontend:
bash
python -m http.server 5501
For backend:
bash
uvicorn backend.app.main:app --reload --port 8001
---

# 17. Recommended Demo Flow

For demonstration:

1. Start Ollama
2. Start backend
3. Start frontend
4. Paste transcript
5. Click Analyze
6. Show summary, decisions, action items
7. Enter GitHub repo details
8. Push tasks to GitHub Issues
9. Open generated issues live

This demonstrates full end-to-end flow.

---

# 18. Acceptance Criteria Mapping

This prototype satisfies:

- transcript ingestion
- key discussion extraction
- at least two action items extraction
- structured task generation
- workflow integration with GitHub Issues
- end-to-end engineering meeting to task flow

---

# 19. Future Improvements

Planned next:
- audio upload
- speech-to-text via Sarvam / Whisper
- live microphone mode
- task editing before push
- Jira integration
- meeting history page
- export reports

---

# 20. Author Notes

This is a prototype designed to demonstrate how engineering meeting discussions can be transformed into structured work items and integrated into developer workflows.

For best results:
- use clean engineering transcripts
- keep Ollama running
- test GitHub token before demo


---

If you want, I can also give you these next:

1. **a cleaner professional README version for submission**
2. **a one-command run script**
   - run_backend.bat
   - run_frontend.bat
   - run_all.sh
3. **requirements.txt final**
4. **sample transcript file**
5. **demo script for presentation**

If you want, next I can generate:
# run_backend.bat, run_frontend.bat, and run_project_steps.md
so you can run everything faster.

Here is a simplified and clean README format (shorter and easier to maintain) in a single file. It keeps the important parts but removes excessive explanations.

You can directly copy this as README.md.

AI Meeting-to-Action System
An AI-powered prototype that converts meeting transcripts into:

Summary

Key discussion points

Decisions

Action items

GitHub Issues

Tech Stack
FastAPI – Backend API

HTML + Tailwind + JS – Frontend

Ollama (Llama 3.1) – Local LLM

SQLite – Storage

GitHub Issues API – Task integration

1. Project Structure
ai-meeting-to-action
│
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schemas.py
│   │   ├── prompts.py
│   │   │
│   │   ├── routes
│   │   │   ├── analyze.py
│   │   │   └── integrations.py
│   │   │
│   │   └── services
│   │       ├── llm_service.py
│   │       └── github_service.py
│   │
│   └── requirements.txt
│
├── frontend
│   ├── index.html
│   └── app.js
│
└── README.md
2. Prerequisites
Install the following:

Python 3.10+

Git

Ollama

GitHub account

Download Ollama:

https://ollama.com/download
3. Setup Project
Create the project folder:

mkdir ai-meeting-to-action
cd ai-meeting-to-action
Create folders:

mkdir backend frontend
mkdir backend/app
mkdir backend/app/routes
mkdir backend/app/services
Create required files and paste the code accordingly.

4. Create Virtual Environment
Windows
python -m venv venv
venv\Scripts\activate
Mac/Linux
python3 -m venv venv
source venv/bin/activate
5. Install Dependencies
pip install -r backend/requirements.txt
Or install manually:

pip install fastapi uvicorn sqlalchemy python-dotenv requests python-multipart pydantic
Check installation:

pip list
6. Setup Ollama
Pull the Llama model:

ollama pull llama3.1
Run the model:

ollama run llama3.1
Check installed models:

ollama list
7. Run Backend
From the project root:

uvicorn backend.app.main:app --reload
Or:

cd backend
uvicorn app.main:app --reload
Backend runs at:

http://127.0.0.1:8000
Swagger docs:

http://127.0.0.1:8000/docs
8. Run Frontend
Open another terminal:

cd frontend
python -m http.server 5500
Open browser:

http://127.0.0.1:5500
9. Correct Run Order
Terminal 1
Start Ollama

ollama run llama3.1
Terminal 2
Run backend

uvicorn backend.app.main:app --reload
Terminal 3
Run frontend

cd frontend
python -m http.server 5500
10. Test the Application
Example transcript:

In today’s sprint planning meeting, the team discussed a login issue that must be fixed before the next release. The backend team will investigate the authentication bug and deploy a fix by Friday. We also agreed that the API needs rate limiting to prevent abuse, and this should be added in the next sprint. The UI team will redesign the dashboard analytics widget to improve readability.
Steps:

Enter meeting title

Paste transcript

Click Analyze Meeting

The system will generate:

Summary

Key Points

Decisions

Action Items

11. GitHub Integration
To push tasks as GitHub Issues:

Go to GitHub Settings

Open Developer Settings

Create Personal Access Token

Required permission:

repo
Enter in UI:

Repo Owner

Repo Name

GitHub Token

Click:

Push Tasks to GitHub Issues
12. Troubleshooting
Backend not starting
Run from backend folder:

cd backend
uvicorn app.main:app --reload
Ollama not responding
Check installation:

ollama list
Restart model:

ollama run llama3.1
Frontend cannot connect to backend
Check backend is running:

http://127.0.0.1:8000
Port already in use
Use different port.

Backend:

uvicorn backend.app.main:app --port 8001
Frontend:

python -m http.server 5501
13. Future Improvements
Audio upload

Speech-to-text

Live microphone recording

Jira integration

Meeting history

Export JSON / Markdown

Author
Prototype demonstrating how meeting discussions can be converted into structured engineering tasks using AI.

✅ This version is cleaner, shorter, and professional for GitHub or project submission.

If you want, I can also give you 3 things that make this project look very professional on GitHub:

README with badges + screenshots

one-command run (run_project.sh)

sample transcript dataset for testing

These greatly improve project presentation for interviews / professors / GitHub portfolio.


can u prepare me a good Readme file for my git hub to display about our project.
there is the content add imogies and make it good

Sure 👍
Below is a professional GitHub README template with emojis, sections, badges, and clean formatting. It is designed to look attractive on GitHub and explain your project clearly.

You can **copy this directly into `README.md



It looks like your last message didn’t include any content. Could you please send the project content or details you want included in


. First: Summary of the Solution
Proposed Solution
We will build an AI Meeting-to-Action System for Engineering Teams that:

Accepts meeting input

pasted transcript
uploaded transcript file
uploaded audio file
optional live microphone recording
Converts audio to text

using Sarvam API or Whisper/local STT if needed
Analyzes the transcript

generate meeting summary
identify key discussion points
extract decisions
extract action items/tasks
structure them into engineering-ready tickets
Displays results in UI

transcript view
summary section
key decisions section
action items/tasks table
push-to-GitHub/Jira button
Integrates with workflow tools

GitHub Issues first (easy and demo-friendly)
Jira optional second integration
maybe Trello/Linear later if time permits
2. Best Practical Version for You
Since you want something buildable and demoable, I recommend this stack:

Frontend
HTML
Tailwind CSS
Vanilla JavaScript
Simple and fast
Backend
FastAPI
Python for AI orchestration and APIs
AI Layer
Llama 3.1 local for:
summarization
decision extraction
action item extraction
task structuring
STT Layer
Choose one:

Sarvam API if it supports speech-to-text for your plan
or Whisper local / whisper.cpp / faster-whisper
For MVP: transcript input can be primary, audio can be secondary
Storage
SQLite for prototype
store meetings, transcripts, action items, pushed tickets
Integration
GitHub Issues API first
Jira optional after MVP
3. Features We Can Add
Here’s a good feature set:

Core Features
Paste transcript
Upload transcript file
Upload audio file
Generate summary
Extract key decisions
Extract action items
Convert to structured tasks
Push tasks to GitHub Issues
Nice Additional Features
Priority detection: High/Medium/Low
Suggested assignee/team extraction
Deadline extraction
Confidence score for extracted tasks
Editable task review before push
Search previous meetings
Download JSON / Markdown meeting report
Slack webhook notification
Duplicate task detection
“Meeting health” score:
number of decisions
unresolved blockers
tasks without owner
Best demo-enhancing features
If you want it to look more impressive:

“Live transcript mode”
“Auto-tag engineering domain”:
bug
feature
tech debt
UI
backend
infrastructure
“Task push history”
4. Final Product Flow
End-to-end flow
Option A: Transcript input
User pastes transcript → backend analyzes with Llama → returns summary + decisions + tasks → user reviews → push to GitHub Issues

Option B: Audio input
User uploads audio → backend sends to STT → transcript generated → backend analyzes using Llama → returns structured output → push to GitHub Issues

Option C: Live mic
Browser records audio → backend converts to transcript chunks → final transcript analyzed → outputs shown

5. Structured Architecture You Should Build
Your architecture is already very good. I would slightly refine it like this:

Presentation Layer
HTML + Tailwind UI
Modules:

Input Panel
Transcript Viewer
Summary View
Decisions View
Action Items Table
Integration Panel
Push History
API Layer (FastAPI)
Endpoints:

POST /analyze-transcript
POST /analyze-audio
POST /integrations/github/push
POST /integrations/jira/push (optional later)
GET /meetings
GET /meetings/{id}
GET /health
AI Processing Layer
Submodules:

Transcript Cleaner
Summarizer
Decision Extractor
Action Item Extractor
Task Structurer
Validation Layer
Data Store
SQLite tables:

meetings
transcripts
summaries
decisions
action_items
task_push_history
External Integrations
Sarvam API / Whisper
GitHub Issues API
Jira Cloud API (optional)
Slack webhook (optional)
6. Recommended Development Strategy
Do not build everything at once.

Build in these phases:

Phase 1 — MVP
Focus only on:

transcript input
local Llama analysis
summary + decisions + action items
show in UI
export JSON
This already satisfies a big part of the problem statement.

Phase 2 — Strong Prototype
Add:

audio upload
speech-to-text
GitHub Issues push
SQLite persistence
Now you satisfy almost all acceptance criteria.

Phase 3 — Demo Polish
Add:

live recording
editable task cards
Jira integration
history page
better prompts / confidence score

Below is a clean, professional GitHub README built from your project description.
It includes emojis, structured sections, architecture, features, and a good presentation style so it looks impressive on GitHub.

You can copy this directly into README.md.

🚀 AI Meeting-to-Action System for Engineering Teams
An AI-powered system that converts engineering meeting discussions into structured tasks and actionable tickets.

This project helps teams transform meeting transcripts or audio recordings into summaries, decisions, and actionable tasks that can be directly pushed to workflow tools like GitHub Issues.

Instead of manually writing meeting notes and creating tasks, the system automatically extracts engineering-ready tickets from conversations using AI.

✨ Key Idea
Engineering meetings often contain:

important technical discussions

design decisions

bug fixes and feature planning

task assignments

However, converting these discussions into structured work items takes time.

This system solves that problem by using AI to automatically convert meetings into action items.

🎯 Features
🧠 AI Meeting Analysis
Generate meeting summary

Identify key discussion points

Extract technical decisions

Detect action items / tasks

Convert tasks into engineering-ready tickets

🎤 Multiple Meeting Input Options
The system supports multiple input formats:

📄 Paste meeting transcript

📂 Upload transcript file (.txt / .srt / .vtt)

🎧 Upload audio recording

🎙 Optional live microphone recording

🔊 Speech-to-Text Support
Audio meetings can be converted to transcripts using:

Sarvam API

OpenAI Whisper / faster-whisper

Local STT models

📊 AI-Generated Output
The system produces structured output:

📝 Meeting Summary

💡 Key Discussion Points

✅ Decisions Taken

📌 Action Items / Tasks

Tasks are displayed in a structured task table.

🔗 Workflow Integration
Tasks can be pushed directly to:

🐙 GitHub Issues (Primary Integration)

🧰 Jira (Optional)

📋 Trello / Linear (Future scope)

🖥️ User Interface
The application provides a clean interface with:

📥 Meeting Input Panel

📜 Transcript Viewer

📑 Summary Section

💡 Decisions Section

📋 Action Items Table

🔗 Push-to-GitHub Button

📊 Task Push History

🧱 Technology Stack
Frontend
HTML

Tailwind CSS

Vanilla JavaScript

Simple, lightweight, and fast UI.

Backend
FastAPI

Python

Handles:

API endpoints

AI orchestration

integrations

AI Layer
Uses Llama 3.1 (local model) for:

meeting summarization

decision extraction

action item detection

task structuring

Speech-to-Text Layer
Options:

Sarvam API

Whisper / faster-whisper

local speech models

Database
SQLite (Prototype storage)

Stores:

meetings

transcripts

summaries

decisions

action items

task push history

🏗 System Architecture
User Interface (HTML + Tailwind)
        │
        ▼
FastAPI Backend
        │
        ├── Transcript Processing
        ├── AI Analysis Layer
        │      ├ Summary Generator
        │      ├ Decision Extractor
        │      ├ Action Item Extractor
        │      └ Task Structurer
        │
        ├── Speech-to-Text (Whisper / Sarvam)
        │
        ├── SQLite Database
        │
        └── External Integrations
              ├ GitHub Issues API
              ├ Jira Cloud API (optional)
              └ Slack Webhooks (optional)
⚙️ API Endpoints
Example backend endpoints:

POST /analyze-transcript
POST /analyze-audio
POST /integrations/github/push
POST /integrations/jira/push
GET  /meetings
GET  /meetings/{id}
GET  /health
🔄 System Workflow
Option 1 — Transcript Input
User pastes transcript
        ↓
Backend sends transcript to AI
        ↓
AI generates summary + decisions + tasks
        ↓
Results displayed in UI
        ↓
User pushes tasks to GitHub Issues
Option 2 — Audio Input
User uploads meeting audio
        ↓
Speech-to-Text generates transcript
        ↓
Transcript analyzed by AI
        ↓
Summary + decisions + action items generated
        ↓
Tasks pushed to GitHub
Option 3 — Live Meeting Mode (Future)
Live microphone recording
        ↓
Real-time transcription
        ↓
Meeting transcript generated
        ↓
AI extracts action items
🌟 Advanced Features
Planned intelligent features:

🎯 Priority detection (High / Medium / Low)

👤 Suggested task assignee detection

⏰ Deadline extraction

📊 Confidence score for tasks

✏ Editable task review before pushing

🔍 Search previous meetings

📤 Export meeting report (JSON / Markdown)

🔔 Slack webhook notifications

📊 Smart Meeting Insights (Future)
The system can also generate:

📈 Meeting Health Score

Number of decisions taken

Unresolved blockers

Tasks without owners

📦 Project Structure
ai-meeting-to-action
│
├── backend
│   ├── app
│   │   ├── main.py
│   │   ├── routes
│   │   ├── services
│   │   ├── models
│   │   └── prompts
│
├── frontend
│   ├── index.html
│   └── app.js
│
└── README.md
🚀 Development Phases
Phase 1 — MVP
transcript input

AI meeting analysis

summary + decisions + tasks

display results in UI

Phase 2 — Prototype
audio upload

speech-to-text

GitHub Issues integration

SQLite database

Phase 3 — Demo Polish
live meeting recording

editable task cards

Jira integration

meeting history dashboard

🎯 Use Cases
This system is useful for:

Software engineering teams

Agile sprint meetings

Technical design discussions

Product planning meetings

Project standups

👨‍💻 Author
Developed as a prototype system demonstrating how AI can convert engineering meetings into structured development tasks.

⭐ Future Scope
Future improvements may include:

live meeting analysis

multi-language transcription

automated sprint planning

deeper integration with developer tools

⭐ If you find this project useful, consider giving it a star on GitHub!

✅ If you want, I can also make an even more impressive GitHub README by adding:

GitHub badges

architecture diagram

UI screenshots section

demo GIF

installation section

These make the project look much more professional on GitHub and during presentations.


can u suggent me good name for the project

Here are some strong project name ideas for your system. I grouped them by style so you can choose depending on whether you want it to sound technical, AI-focused, or product-like.

🚀 AI / Tech-Focused Names
These sound research-oriented and professional (good for papers, demos, and GitHub).

ActionAI

Meet2Task AI

ActionForge AI

MeetSense AI

TaskMind AI

Discuss2Deploy

ActionGraph AI

TaskSynth AI

⭐ Best picks:

Meet2Task AI

ActionForge AI

TaskMind AI

🧠 AI Meeting Assistant Style
These emphasize meeting intelligence and analysis.

MeetIntel

MeetingMind

InsightMeet

MeetWise AI

MeetLogic

⭐ Best picks:

MeetIntel

MeetingMind

⚙️ Engineering / Developer Style
These sound like developer tools.

SprintScribe

DevMeet AI

TaskBridge

DevAction AI

CodeMeet Assistant

⭐ Best picks:

SprintScribe

TaskBridge

🤖 Product-Style Names (Best for Demo)
These sound like real startup tools.

ActionFlow AI

TaskPilot AI

MeetFlow AI

ActionSync

TaskGenie

⭐ Best picks:

ActionFlow AI

TaskPilot AI

MeetFlow AI

🏆 My Top 5 Recommendations (Best Overall)
If this were my project, I would choose one of these:

ActionForge AI ⭐ (very strong and unique)

Meet2Task AI ⭐ (perfectly describes your system)

SprintScribe ⭐ (great for engineering teams)

TaskPilot AI ⭐ (startup-style name)

MeetFlow AI

💡 My #1 suggestion for your project:

🚀 Meet2Task AI — Turning Meetings into Actionable Engineering Tasks

It is:

very clear

easy to remember

perfect for GitHub + presentation

explains the purpose immediately.

If you want, I can also help you create:

a cool project tagline

GitHub repo description

logo idea

project slogan for your presentation

These make the project look much more professional during demos or competitions.


TaskMind this is good now give me the full read me file text in a single format

Below is a complete GitHub README.md for your project named “TaskMind”.
It is written in a single clean format, ready to copy-paste directly into GitHub.
It includes emojis, structure, and a professional layout.

🧠 TaskMind
AI Meeting-to-Action System for Engineering Teams
TaskMind is an AI-powered system that transforms meeting discussions into structured engineering tasks.

Instead of manually writing meeting notes and creating tickets, TaskMind automatically analyzes meeting transcripts or audio recordings to generate summaries, decisions, and actionable tasks that can be pushed directly to workflow tools like GitHub Issues.

🚀 Project Overview
Engineering meetings often include:

technical discussions

feature planning

bug analysis

architectural decisions

task assignments

However, converting these conversations into clear and actionable development tasks is often time-consuming.

TaskMind solves this problem by using AI to automatically extract structured action items from meeting discussions.

✨ Key Features
🧠 AI Meeting Analysis
TaskMind uses AI models to automatically analyze meeting content and generate:

📝 Meeting Summary

💡 Key Discussion Points

✅ Decisions Taken

📌 Action Items / Tasks

These tasks are structured so they can easily be converted into engineering tickets.

🎤 Multiple Meeting Input Options
TaskMind supports several input formats:

📄 Paste meeting transcript

📂 Upload transcript files (.txt / .vtt / .srt)

🎧 Upload meeting audio recordings

🎙 Optional live microphone recording (future feature)

🔊 Speech-to-Text Processing
For audio meetings, TaskMind converts speech into text using:

Sarvam API

Whisper / faster-whisper

Local speech-to-text models

After transcription, the AI analyzes the meeting content.

📊 Structured Output
After analysis, TaskMind presents results in a structured format:

Meeting transcript viewer

AI-generated summary

Key decisions section

Action items table

Each action item can later be pushed to external workflow tools.

🔗 Workflow Integration
TaskMind integrates with engineering tools to create real development tasks.

Supported integrations:

🐙 GitHub Issues (primary integration)

🧰 Jira Cloud (optional)

📋 Trello / Linear (future scope)

Users can review tasks and push them directly as GitHub Issues.

🖥 User Interface
The system provides a simple and clean web interface including:

📥 Meeting Input Panel

📜 Transcript Viewer

📑 Summary Section

💡 Decisions Section

📋 Action Items Table

🔗 Push-to-GitHub Button

📊 Task Push History

🧱 Technology Stack
Frontend
HTML

Tailwind CSS

Vanilla JavaScript

Lightweight UI designed for simplicity and fast prototyping.

Backend
FastAPI

Python

Handles:

API endpoints

AI orchestration

integrations with external tools

AI Processing Layer
TaskMind uses Llama 3.1 (local LLM) to perform:

meeting summarization

decision extraction

action item detection

task structuring

Speech-to-Text Layer
Supported speech processing tools:

Sarvam API

Whisper / faster-whisper

Local STT models

Database
SQLite is used for prototype data storage.

Stored information includes:

meetings

transcripts

summaries

decisions

action items

task push history

🏗 System Architecture
User Interface (HTML + Tailwind)
        │
        ▼
FastAPI Backend
        │
        ├── Transcript Processing
        │
        ├── AI Processing Layer
        │      ├ Summary Generator
        │      ├ Decision Extractor
        │      ├ Action Item Extractor
        │      └ Task Structurer
        │
        ├── Speech-to-Text Layer
        │      ├ Sarvam API
        │      └ Whisper
        │
        ├── SQLite Database
        │
        └── Integrations
               ├ GitHub Issues API
               ├ Jira Cloud API (optional)
               └ Slack Webhooks (future)
⚙️ Backend API Endpoints
Example API endpoints used in TaskMind:

POST /analyze-transcript
POST /analyze-audio
POST /integrations/github/push
POST /integrations/jira/push
GET  /meetings
GET  /meetings/{id}
GET  /health
🔄 System Workflow
Option 1 — Transcript Input
User pastes meeting transcript
        ↓
Backend sends transcript to AI model
        ↓
AI generates summary, decisions, and tasks
        ↓
Results displayed in UI
        ↓
User reviews tasks
        ↓
Tasks pushed to GitHub Issues
Option 2 — Audio Input
User uploads meeting audio
        ↓
Speech-to-text converts audio to transcript
        ↓
AI analyzes transcript
        ↓
Summary + decisions + action items generated
        ↓
Tasks pushed to GitHub Issues
🌟 Advanced Features (Future Enhancements)
Planned intelligent capabilities include:

🎯 Priority detection (High / Medium / Low)

👤 Suggested task assignee extraction

⏰ Deadline detection

📊 Confidence score for extracted tasks

✏ Editable task cards before pushing

🔍 Search previous meetings

📤 Export meeting reports (JSON / Markdown)

🔔 Slack webhook notifications

📊 Smart Meeting Insights (Future)
TaskMind may also generate meeting analytics such as:

📈 Meeting Health Score

Number of decisions made

Unresolved blockers

Tasks without owners

📦 Project Structure
meeting-assistant/
│
├── backend/
│   │
│   │   ── MEMBER 1's FILES ──
│   ├── audio_capture.py              ← Captures system audio + force_stop()
│   ├── transcriber.py                ← Whisper speech to text
│   ├── file_parser.py                ← Parses .vtt / .srt / .txt files
│   │
│   │   ── MEMBER 2's FILES ──
│   ├── main.py                       ← FastAPI server (connects everything)
│   ├── analyzer.py                   ← Ollama AI meeting analysis
│   ├── chatbot.py                    ← Chatbot Q&A about meeting
│   ├── calendar_service.py           ← NEW — Reads Google/Notion calendar
│   ├── scheduler.py                  ← NEW — Auto start/stop based on calendar
│   ├── jira_integration.py           ← NEW — Creates Jira tickets (replaces GitHub)
│   ├── database.py                   ← SQLite meeting history storage
│   ├── requirements.txt              ← All Python dependencies
│   └── .env                          ← API keys and config
│
├── frontend/
│   │
│   │   ── MEMBER 3's FILES ──
│   ├── index.html                    ← Chat UI + Kill/Restart button + notifications
│   ├── style.css                     ← Styling (dark theme)
│   └── app.js                        ← Chat logic + WebSocket + calendar display
│
├── credentials.json                  ← Google Calendar OAuth (only if using Google)
├── meetings.db                       ← SQLite database (auto-created when app runs)
├── README.md                         ← MEMBER 3 — Project documentation
├── architecture-diagram.png          ← MEMBER 3 — System diagram
└── uploads/                          ← Auto-created folder for uploaded audio files

