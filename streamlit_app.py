import streamlit as st
from datetime import datetime
import requests  # Standard in Streamlit Cloud

# Krasses Sci-Fi-Design
st.set_page_config(page_title="J.A.R.V.I.S.", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""
<style>
    .main {background: linear-gradient(135deg, #0e0e1f 0%, #1a1a3d 100%) !important;}
    .stApp {background: transparent !important;}
    h1 {font-family: 'Orbitron', sans-serif; text-align: center; color: #00ffff; 
        text-shadow: 0 0 30px #00ffff; font-size: 4rem; margin: 0;}
    .subtitle {text-align: center; color: #00ffaa; font-size: 1.5rem; font-style: italic;}
    .status {text-align: center; color: #ffff00; font-size: 1.2rem; font-weight: bold;}
    .mic-btn {background: radial-gradient(circle, #4b0082, #8a2be2); color: white; 
              padding: 20px; font-size: 2rem; border-radius: 50%; width: 200px; height: 200px; 
              border: 3px solid #00ffff; box-shadow: 0 0 40px #00ffff; cursor: pointer; transition: all 0.3s;}
    .mic-btn:hover {transform: scale(1.1); box-shadow: 0 0 60px #8a2be2;}
    .output {background: rgba(0, 255, 255, 0.1); border: 1px solid #00ffff; border-radius: 10px; padding: 15px; color: #00ffaa; font-family: 'Courier New', monospace;}
</style>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown("<h1>J.A.R.V.I.S.</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Just A Rather Very Intelligent System</p>", unsafe_allow_html=True)

# Status
st.markdown("<p class='status' id='status'>Online und bereit, Sir.</p>", unsafe_allow_html=True)

# Spracherkennung + TTS im Browser (keine Bibliothek nötig)
st.markdown("""
<script>
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'de-DE';
recognition.onresult = function(e) {
    const command = e.results[0][0].transcript.toLowerCase();
    document.getElementById('command').value = command;
    document.getElementById('submit').click();
    speakResponse('Befehl erkannt: ' + command);  // Vorschau-Sprache
};
function startListening() {
    recognition.start();
    document.getElementById('status').innerHTML = 'Ich höre zu...';
}
function speakResponse(text) {
    const utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'de-DE';
    utterance.rate = 1.2;
    utterance.pitch = 0.8;
    speechSynthesis.speak(utterance);
}
</script>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown('<button class="mic-btn" onclick="startListening()">🎤 SPRICH JETZT</button>', unsafe_allow_html=True)

# Befehl verarbeiten
command = st.text_input("Oder tippe hier:", key="command", label_visibility="collapsed")
if st.button("Ausführen", key="submit", type="primary"):
    if command:
        command = command.lower().strip()
        st.markdown(f"<p class='status'>Verarbeite: {command}</p>", unsafe_allow_html=True)

        #
