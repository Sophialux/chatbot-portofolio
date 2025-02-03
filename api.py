from fastapi import FastAPI
import ollama

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Bienvenue sur mon API IA avec Ollama et FastAPI"}

@app.post("/chat")
def chat(prompt: str):
    response = ollama.chat(model="mistral", messages=[{"role": "user", "content": prompt}])
    return {"response": response['message']['content']}