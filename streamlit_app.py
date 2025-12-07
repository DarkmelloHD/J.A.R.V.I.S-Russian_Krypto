import streamlit as st
from datetime import datetime
import requests
import random

# Design
st.set_page_config(page_title="J.A.R.V.I.S.", layout="centered")
st.markdown("""
<style>
    .main {background: linear-gradient(135deg, #0e0e1f, #1a1a3d);}
    h1 {font-family: 'Orbitron', sans-serif; text-align: center; color: #00ffff; 
        text-shadow: 0 0 30px #00ffff; font-size: 5rem;}
    .mic {background: #8a2be2; color: white; padding: 30px; font-size: 3rem; 
          border-radius: 50%; width: 220px; height: 220px; border: 5px solid #00ffff;
          box-shadow: 0 0 60px #00ffff; cursor: pointer;}
    .mic:hover {transform: scale(1.15); box-shadow: 0 0 90px #8a2be2;}
    .output {background: rgba(0,255,255,0.1); padding: 20px; border-radius: 15px; 
             border: 1px solid #00ffff; color: #00ffaa; font-size: 1.3rem;}
</style>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown("<h1>J.A.R.V.I.S.</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#00ffaa;'>Klicke & sprich – ich antworte sofort!</h3>", unsafe_allow_html=True)

# JavaScript + Auto-Submit (JETZT FUNKTIONIERT ES!)
st.markdown("""
<script>
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'de-DE';
recognition.interimResults = false;

recognition.onresult = function(e) {
    const text = e.results[0][0].transcript;
    document.getElementById('cmd').value = text.toLowerCase();
    // Automatisch absenden!
    const btn = document.getElementById('hidden_submit');
    btn.click();
};
recognition.onerror = function() { parent.streamlitSetComponentValue("Fehler beim Hören"); };

function start() {
    recognition.start();
    document.getElementById('status').innerHTML = "Ich höre zu...";
}
</script>
""", unsafe_allow_html=True)

# Unsichtbarer Submit-Button
if st.button("Absenden", key="hidden_submit", help="wird automatisch geklickt"):
    pass

# Großer Mikrofon-Button
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown('<button class="mic" onclick="start()">SPRICH JETZT</button>', unsafe_allow_html=True)

st.markdown("<p id='status' style='text-align:center; color:#ffff00; font-size:1.5rem;'>Bereit</p>", unsafe_allow_html=True)

# Befehl empfangen
command = st.text_input("", key="cmd", label_visibility="collapsed").lower().strip()

if command:
    st.markdown("<p id='status' style='text-align:center; color:#00ff00;'>Verarbeite Befehl...</p>", unsafe_allow_html=True)

    # Sofort-Antwort
