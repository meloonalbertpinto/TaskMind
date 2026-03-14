window.onerror = function(msg, url, lineNo, columnNo, error) {
    alert('Error: ' + msg + '\nLine: ' + lineNo);
    return false;
};
console.log('Script starting...');
lucide.createIcons();

let isRecording = false;
let socket = null;
const recordBtn = document.getElementById('record-btn');
const stopBtn = document.getElementById('stop-btn');
const btnIcon = document.getElementById('btn-icon');
const recordingIndicator = document.getElementById('recording-indicator');
const recordingLabel = document.getElementById('recording-label');
const transcriptContainer = document.getElementById('transcript-container');
const emptyState = document.getElementById('empty-state');
const statusDot = document.getElementById('status-dot');
const statusText = document.getElementById('status-text');
const clearBtn = document.getElementById('clear-btn');
const analyzeBtn = document.getElementById('analyze-btn');
const modeSelect = document.getElementById('mode-select');
const langSelect = document.getElementById('lang-select');
const langContainer = document.getElementById('lang-container');
const headerTitle = document.getElementById('header-title');

// Insights elements
const insightsContainer = document.getElementById('insights-container');
const insightsLoading = document.getElementById('insights-loading');
const insightsResults = document.getElementById('insights-results');
const closeInsights = document.getElementById('close-insights');

const resSummary = document.getElementById('res-summary');
const resPoints = document.getElementById('res-points');
const resActions = document.getElementById('res-actions');
const resDecisions = document.getElementById('res-decisions');

// Q&A elements
const qaChatHistory = document.getElementById('qa-chat-history');
const qaInput = document.getElementById('qa-input');
const qaSendBtn = document.getElementById('qa-send-btn');

modeSelect.addEventListener('change', () => {
    if (modeSelect.value === 'transcribe') {
        langContainer.classList.remove('hidden');
        headerTitle.innerText = 'Smart Live Transcription';
    } else {
        langContainer.classList.add('hidden');
        headerTitle.innerText = 'Universal Live Translation';
    }
});

function connectWebSocket() {
    const protocol = window.location.protocol === 'https:' ? 'wss:' : 'ws:';
    socket = new WebSocket(`${protocol}//${window.location.host}/ws`);

    socket.onopen = () => {
        statusDot.classList.replace('bg-gray-500', 'bg-emerald-500');
        statusDot.classList.remove('bg-red-500');
        statusText.innerText = 'Connected';
        statusText.classList.replace('text-gray-400', 'text-emerald-400');
    };

    socket.onclose = () => {
        statusDot.classList.replace('bg-emerald-500', 'bg-red-500');
        statusText.innerText = 'Disconnected';
        statusText.classList.replace('text-emerald-400', 'text-red-400');
        setTimeout(connectWebSocket, 3000);
    };

    socket.onmessage = (event) => {
        addTranscript(event.data);
    };
}

function addTranscript(text) {
    if (!text.trim()) return;
    emptyState.classList.add('hidden');
    
    const div = document.createElement('div');
    const isTranslate = modeSelect.value === 'translate';
    div.className = `message-entry glass p-4 rounded-2xl border-l-4 ${isTranslate ? 'border-blue-500' : 'border-purple-500'} bg-white/5`;
    
    const time = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    const label = isTranslate ? 'English Translation' : 'Transcript';
    
    div.innerHTML = `
        <div class="flex justify-between items-start mb-1">
            <span class="text-xs font-semibold ${isTranslate ? 'text-blue-400' : 'text-purple-400'} uppercase tracking-wider">${label}</span>
            <span class="text-[10px] text-gray-500">${time}</span>
        </div>
        <p class="text-gray-200 leading-relaxed">${text}</p>
    `;
    
    transcriptContainer.appendChild(div);
    transcriptContainer.scrollTop = transcriptContainer.scrollHeight;
}

async function startTranscription() {
    const config = {
        mode: modeSelect.value,
        language: modeSelect.value === 'translate' ? 'unknown' : langSelect.value
    };

    try {
        const res = await fetch('/start', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(config)
        });

        if (res.ok) {
            isRecording = true;
            updateUI(true);
        }
    } catch (e) {
        console.error("Failed to start", e);
    }
}

async function stopTranscription() {
    try {
        const res = await fetch('/stop', { method: 'POST' });
        if (res.ok) {
            isRecording = false;
            updateUI(false);
        }
    } catch (e) {
        console.error("Failed to stop", e);
    }
}

function updateUI(active) {
     if (active) {
        recordBtn.classList.replace('bg-white', 'bg-emerald-500');
        btnIcon.innerHTML = '<path d="M12 2a3 3 0 0 0-3 3v7a3 3 0 0 0 6 0V5a3 3 0 0 0-3-3Z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" x2="12" y1="19" y2="22"></line>';
        btnIcon.classList.replace('text-gray-900', 'text-white');
        btnIcon.classList.remove('fill-gray-900');
        recordingIndicator.classList.remove('hidden');
        recordingLabel.innerText = 'Bot is Listening...';
        recordingLabel.classList.replace('text-gray-400', 'text-emerald-400');
        stopBtn.classList.remove('hidden');
    } else {
        recordBtn.classList.replace('bg-emerald-500', 'bg-white');
        btnIcon.innerHTML = '<polygon points="5 3 19 12 5 21 5 3"></polygon>';
        btnIcon.classList.replace('text-white', 'text-gray-900');
        btnIcon.classList.add('fill-gray-900');
        recordingIndicator.classList.add('hidden');
        recordingLabel.innerText = 'Session Stopped. Click Play to start again.';
        recordingLabel.classList.replace('text-emerald-400', 'text-gray-400');
        stopBtn.classList.add('hidden');
    }
    lucide.createIcons();
}

recordBtn.addEventListener('click', () => {
    if (!isRecording) startTranscription();
    else startTranscription(); // Allow updating settings while running
});

stopBtn.addEventListener('click', stopTranscription);

clearBtn.addEventListener('click', async () => {
    if (confirm('Clear all transcripts and history?')) {
        await fetch('/clear', { method: 'POST' });
        transcriptContainer.innerHTML = '';
        emptyState.classList.remove('hidden');
        transcriptContainer.appendChild(emptyState);
        insightsContainer.classList.add('hidden');
    }
});

async function handleAnalyze() {
    console.log('Analyze triggered');
    insightsContainer.classList.remove('hidden');
    insightsLoading.classList.remove('hidden');
    insightsResults.classList.add('hidden');
    analyzeBtn.disabled = true;

    try {
        const res = await fetch('/analyze', { method: 'POST' });
        const data = await res.json();
        console.log('Analysis data received:', data);
        
        if (data.error) {
            insightsLoading.classList.add('hidden');
            insightsResults.classList.remove('hidden');
            resSummary.innerHTML = `<span class="text-red-400">Error: ${data.error}</span>`;
            resPoints.innerHTML = '';
            resActions.innerHTML = '';
            resDecisions.innerHTML = '';
        } else {
            displayInsights(data);
        }
    } catch (e) {
        console.error("Failed to analyze", e);
        alert('Connection error during analysis: ' + e.message);
    } finally {
        insightsLoading.classList.add('hidden');
        analyzeBtn.disabled = false;
    }
}

async function handleAsk() {
    const question = qaInput.value.trim();
    if (!question) return;

    qaInput.value = '';
    qaSendBtn.disabled = true;

    // Add user question to history
    addQaMessage('You', question);

    try {
        const res = await fetch('/ask', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question })
        });
        const data = await res.json();

        if (data.error) {
            addQaMessage('AI', 'Error: ' + data.error);
        } else if (data.answer) {
            addQaMessage('AI', data.answer);
        }
    } catch (e) {
        console.error("Failed to ask question", e);
        addQaMessage('AI', 'Connection error.');
    } finally {
        qaSendBtn.disabled = false;
    }
}

function addQaMessage(sender, text) {
    const div = document.createElement('div');
    div.className = sender === 'You' ? 'bg-blue-500/10 p-3 rounded-xl border border-blue-500/20' : 'bg-white/5 p-3 rounded-xl border border-white/5';
    div.innerHTML = `
        <p class="text-[10px] font-bold ${sender === 'You' ? 'text-blue-400' : 'text-purple-400'} uppercase mb-1">${sender}</p>
        <p class="text-xs text-gray-300 leading-relaxed whitespace-pre-line">${text}</p>
    `;
    qaChatHistory.appendChild(div);
    qaChatHistory.scrollTop = qaChatHistory.scrollHeight;
}

analyzeBtn.onclick = handleAnalyze;
qaSendBtn.onclick = handleAsk;
qaInput.onkeypress = (e) => {
    if (e.key === 'Enter') handleAsk();
};

closeInsights.addEventListener('click', () => {
    insightsContainer.classList.add('hidden');
});

function displayInsights(data) {
    insightsResults.classList.remove('hidden');
    
    resSummary.innerText = data.summary || 'No summary available';
    
    resPoints.innerHTML = (data.key_points || []).map(p => `<li>${p}</li>`).join('') || '<li>None identified</li>';
    resActions.innerHTML = (data.action_items || []).map(a => `<li>${a}</li>`).join('') || '<li>None identified</li>';
    resDecisions.innerHTML = (data.key_decisions || []).map(d => `<li>${d}</li>`).join('') || '<li>None identified</li>';
    
    lucide.createIcons();
}

// Initialize
connectWebSocket();
