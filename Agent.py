import streamlit as st
import os
import requests
import pandas as pd
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import re

# 🔐 Charger le token Hugging Face
dotenv_path = ".env"
load_dotenv(dotenv_path)
HF_TOKEN = os.getenv("HF_TOKEN")

# 📙 Charger les données (corrigé)
data = pd.read_csv("base_voyage.txt", sep=";", encoding="utf-8-sig")
data.columns = data.columns.str.strip().str.lower()  # Nettoyer les noms de colonnes
print("Colonnes lues :", data.columns.tolist())

questions = data["question"].tolist()
reponses = data["reponse"].tolist()

# 🔍 Embedding
model = SentenceTransformer("all-MiniLM-L6-v2")
question_embeddings = model.encode(questions)

# 🧐 Index FAISS
dimension = question_embeddings.shape[1]
index = faiss.IndexFlatL2(dimension)
index.add(np.array(question_embeddings))

# 🪨 Fonction de RAG améliorée (corrections ici)
def retrieve_context(user_input, top_k=3, max_words=500):
    input_embedding = model.encode([user_input])
    distances, indices = index.search(np.array(input_embedding), top_k)

    contexts = []
    premier_pays = None #Pour mémoriser le premier pays trouvé

    for idx, dist in zip(indices[0], distances[0]):
        if idx < len(reponses):
            clean_text = re.sub(r"\s+", " ", reponses[idx]).strip()
            contexts.append(clean_text)
            
            if premier_pays is None:
                premier_pays= data.iloc[idx]["pays"] #on extrat le pays associé

    full_context = " ".join(contexts)
    truncated = " ".join(full_context.split()[:max_words])
    return truncated, premier_pays

# 🔗 Appel à l'API HF corrigé (corrections ici aussi)
def query_huggingface_with_context(user_input, context):
    API_URL = "https://router.huggingface.co/together/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {HF_TOKEN}",
        "Content-Type": "application/json"
    }

    prompt = f"Voici un contexte de voyage : {context}\n\nRéponds à la question suivante : {user_input}"

    payload = {
        "model": "mistralai/Mixtral-8x7B-Instruct-v0.1",
        "messages": [
            {"role": "system", "content": "Tu es un assistant de voyage chaleureux et professionnel. Tu réponds toujours en te basant uniquement sur les informations fournies dans le contexte, sans inventer. Si le contexte parle d'un pays en particulier, tu dois répondre en te concentrant sur ce pays."},
            #{"role": "system", "content": "Tu es un assistant de voyage professionnel. Réponds aux questions de manière claire, précise, utile et adaptée au contexte du voyage."},
            {"role": "user", "content": prompt}
        ],
        "max_tokens": 600,
        "temperature": 0.7  # ✅ Attention : doit être float, pas string
    }

    print("\U0001f4be Prompt envoyé au modèle :")
    print(prompt[:300])  # ✅ Affichage partiel pour debug

    try:
        response = requests.post(API_URL, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Erreur Hugging Face : {response.status_code} - {response.text}"
    except Exception as e:
        return f"Erreur Hugging Face : {str(e)}"

# 🌈 Thème visuel
primary_color = "#B66878"
gray_color = "#f0f0f0"
background = gray_color
user_bubble = "#3A3F44"
assistant_bubble = "#B66878"
text_color = "#FFFFFF"

st.set_page_config(page_title="VoyageBot", layout="centered")

st.markdown(f"""
    <style>
    body {{
        background-color: {background};
        color: {text_color};
    }}
    .chat-bubble {{
        padding: 0.8em 1.2em;
        border-radius: 1em;
        margin-bottom: 1em;
        max-width: 80%;
        font-size: 1rem;
        line-height: 1.4;
    }}
    .user {{
        background-color: {user_bubble};
        align-self: flex-end;
        margin-left: auto;
    }}
    .assistant {{
        background-color: {assistant_bubble};
        align-self: flex-start;
        margin-right: auto;
    }}
    .chat-container {{
        display: flex;
        flex-direction: column;
    }}
    </style>
""", unsafe_allow_html=True)

#st.title("✈️ Bot Voyage - pour un bon voyage")

st.markdown("""
    <h1 style='color: #B66878; font-size: 3em;'>
        ✈️ BotVoyage
        <span style='font-size: 0.6em; font-style: italic; color: #666666;'>
            — pour un bon voyage
        </span>
    </h1>
""", unsafe_allow_html=True)


# 💬 Historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# 🛅 Entrée utilisateur
user_input = st.chat_input("Pose-moi une question sur le voyage...")

if user_input:
    #ajouter le dernier pays montionné si disponible
    if "dernier_pays" in st.session_state:
        user_input=f"{user_input} (Pays: {st.session_state['dernier_pays']})"
        
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    with st.spinner("💭 Je réfléchis avec mes connaissances voyage..."):
        context, pays_trouve = retrieve_context(user_input)
        
        # mémoriser le nouveau pays s'il existe
        if pays_trouve:
            st.session_state['dernier_pays'] = pays_trouve
            
        response = query_huggingface_with_context(user_input, context)
    st.session_state.messages.append({"role": "assistant", "content": response})

# 💬 Affichage du chat
for msg in st.session_state.messages:
    role = msg["role"]
    content = msg["content"]
    css_class = "user" if role == "user" else "assistant"
    st.markdown(
        f"<div class='chat-container'><div class='chat-bubble {css_class}'>{content}</div></div>",
        unsafe_allow_html=True
    )
