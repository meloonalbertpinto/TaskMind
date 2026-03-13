```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>TaskMind README</title>
</head>
<body>

  <h1>🧠 TaskMind</h1>
  <h3>AI Meeting-to-Action System for Engineering Teams</h3>

  <p>
    <strong>TaskMind</strong> is an AI-powered system that converts meeting discussions into
    structured engineering tasks. It analyzes meeting transcripts or audio recordings to generate
    summaries, decisions, and actionable tasks that can be pushed to tools like GitHub Issues.
  </p>

  <hr />

  <h2>🚀 Project Overview</h2>
  <p>
    Engineering meetings often include technical discussions, feature planning, bug analysis,
    architectural decisions, and task assignments. TaskMind simplifies this process by automatically
    extracting useful and actionable development tasks from meetings.
  </p>

  <h2>✨ Key Features</h2>
  <ul>
    <li>📝 AI-generated meeting summary</li>
    <li>💡 Key discussion points extraction</li>
    <li>✅ Decision detection</li>
    <li>📌 Action item / task extraction</li>
    <li>📄 Transcript input support</li>
    <li>🎧 Audio input support with speech-to-text</li>
    <li>🔗 GitHub Issues integration</li>
  </ul>

  <h2>🛠️ Tech Stack</h2>
  <ul>
    <li><strong>Frontend:</strong> HTML, Tailwind CSS, JavaScript</li>
    <li><strong>Backend:</strong> FastAPI, Python</li>
    <li><strong>AI Model:</strong> Llama 3.1</li>
    <li><strong>Speech-to-Text:</strong> Sarvam API / Whisper / faster-whisper</li>
    <li><strong>Database:</strong> SQLite</li>
  </ul>

  <h2>🏗️ System Architecture</h2>
  <pre>
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
  </pre>

  <h2>⚙️ Main API Endpoints</h2>
  <ul>
    <li><code>POST /analyze-transcript</code></li>
    <li><code>POST /analyze-audio</code></li>
    <li><code>POST /integrations/github/push</code></li>
    <li><code>GET /meetings</code></li>
    <li><code>GET /health</code></li>
  </ul>

  <h2>🔄 Workflow</h2>
  <ol>
    <li>User uploads or pastes meeting content</li>
    <li>Speech-to-text converts audio if needed</li>
    <li>AI analyzes transcript</li>
    <li>System generates summary, decisions, and tasks</li>
    <li>User reviews and pushes tasks to GitHub Issues</li>
  </ol>

  <h2>📌 Future Enhancements</h2>
  <ul>
    <li>🎯 Priority detection</li>
    <li>👤 Suggested assignee extraction</li>
    <li>⏰ Deadline detection</li>
    <li>📤 Export reports</li>
    <li>🔔 Slack notifications</li>
  </ul>

  <h2>👨‍💻 Author</h2>
  <p>
    Developed as a prototype to demonstrate how AI can transform engineering meeting discussions
    into structured development tasks.
  </p>

</body>
</html>
```
