import streamlit as st
import ollama  # Utiliser Ollama au lieu d'OpenAI

# Configurer Streamlit
st.set_page_config(page_title="Chatbot IA en local", page_icon="🤖")

st.title("🤖 Chatbot IA avec Ollama (Mistral)")
st.write("Pose-moi une question et je vais y répondre en français !")

# Zone de texte pour l'utilisateur
user_input = st.text_area("💬 Tape ta question ici :")

if st.button("Envoyer"):
    if user_input.strip():
        # Forcer l'IA à répondre en français
        prompt = f"Réponds uniquement en français et évite toute autre langue. {user_input}"

        # Envoi de la requête à Ollama
        response = ollama.chat(
            model="mistral",
            messages=[{"role": "user", "content": prompt}]
        )

        # Affichage de la réponse
        st.subheader("🧠 Réponse du Chatbot :")
        st.write(response["message"]["content"])
    else:
        st.warning("⚠️ Écris une question avant d'envoyer !")