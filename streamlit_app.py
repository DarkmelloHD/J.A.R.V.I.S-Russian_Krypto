import streamlit as st
from datetime import datetime
import base64
import io
from gtts import gTTS

# Krasses Design
st.set_page_config(page_title="J.A.R.V.I.S.", layout="centered")
st.markdown("""
<style>
    .main {background: #0e0e1f !important;}
    .stApp {background: linear-gradient(135deg, #0e0e1f, #1a1a3d);}
    h1 {font-family: 'Orbitron', sans-serif; text-align: center; color: #00ffff; 
        text-shadow: 0 0 30px #00ffff; font-size: 5rem; margin-bottom: 0;}
    .mic-btn {background: #4b0082; color: white; padding: 30px; font-size: 2.5rem; 
              border-radius: 50%; width: 220px; height: 220px; border: 5px solid #00ffff;
              box-shadow: 0 0 50px #00ffff; cursor: pointer;}
    .mic-btn:hover {background: #8a2be2; box-shadow: 0 0 80px #8a2be2; transform: scale(1.1);}
</style>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@700&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown("<h1>J.A.R.V.I.S.</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align:center; color:#00ffaa;'>Just A Rather Very Intelligent System</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#888; font-size:1.2rem;'>Klicke auf den Button und sprich!</p>", unsafe_allow_html=True)

# Spracherkennung im Browser
st.markdown("""
<script>
const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'de-DE';
recognition.onresult = function(e) {
    document.getElementById('command').value = e.results[0][0].transcript;
    document.getElementById('submit').click();
};
function start() {
    recognition.start();
    document.getElementById('status').innerHTML = "Ich höre zu...";
}
</script>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.markdown("<h2 style='text-align:center; color:#ffff00' id='status'>Bereit</h2>", unsafe_allow_html=True)
    st.markdown('<button class="mic-btn" onclick="start()">SPRICH JETZT</button>', unsafe_allow_html=True)

# Befehl empfangen
command = st.text_input("", key="command", label_visibility="collapsed")
if command:
    command = command.lower().strip()

    if "zeit" in command or "uhr" in command:
        antwort = f"Es ist {datetime.now().strftime('%H:%M Uhr')}."
    elif "wetter" in command:
        stadt = command.split("in")[-1].strip() if "in" in command else "deiner Stadt"
        antwort = f"In {stadt} ist es aktuell schön – ich habe keine API, aber ich glaube an dich!"
    elif "witz" in command:
        antwort = "Warum können Geister so schlecht lügen? Weil man durch sie hindurchsieht!"
    elif "spotify" in command or "musik" in command:
        antwort = "Spotify wird geöffnet..."
        st.markdown("[Spotify starten](https://open.spotify.com)")
    elif "hallo" in command or "hey" in command:
        antwort = "Sir, ich bin online. Wie kann ich helfen?"
    else:
        antwort = f"Ich habe verstanden: '{command}'. Funktion kommt bald!"

    # Jarvis spricht!
    tts = gTTS(antwort, lang="de")
    audio = io.BytesIO()
    tts.write_to_fp(audio)
    audio.seek(0)
    b64 = base64.b64encode(audio.read()).decode()
    st.audio(f"data:audio/mp3;base64,{b64}", format="audio/mp3")
    st.success(f"Jarvis: {antwort}")
