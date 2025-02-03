import streamlit as st
import requests

# Configuration de l'interface
st.set_page_config(page_title="Chatbot IA avec Ollama", page_icon="🤖", layout="centered")

st.title("🤖 Chatbot IA avec Ollama (Mistral)")
st.write("Pose-moi une question et je vais y répondre en français !")

# Zone de texte pour poser une question
user_input = st.text_area("💬 Tape ta question ici :")

if st.button("Envoyer"):
    if user_input.strip():
        # Envoi de la requête à l'API FastAPI
        response = requests.post("http://localhost:8000/chat", params={"prompt": user_input})

        if response.status_code == 200:
            bot_response = response.json().get("response", "Erreur dans la réponse de l'IA")
            st.subheader("🧠 Réponse du Chatbot :")
            st.write(bot_response)
        else:
            st.error("❌ Erreur lors de la communication avec l'API.")
    else:
        st.warning("⚠️ Écris une question avant d'envoyer !")