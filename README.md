# 🧠 Mon Agent LLM (gratuit avec Hugging Face)

Ce projet est un **agent conversationnel intelligent**, construit avec un modèle LLM open-source hébergé sur Hugging Face et enrichi par une base de connaissances via RAG (Retrieval-Augmented Generation).

---

## 🔧 Objectif du projet

Créer un chatbot qui :
- Utilise un modèle open-source (`Mixtral-8x7B-Instruct`)
- Fonctionne gratuitement via l’API Inference de Hugging Face
- Est enrichi par une base de données locale (RAG)
- Peut être utilisé dans le terminal ou via une interface Streamlit
- Est facile à personnaliser


---


## 📚 Fonctionnement général

L’agent utilise une combinaison de techniques :
- 🔎 **FAISS** pour retrouver les documents les plus pertinents dans une base locale (questions-réponses)
- 🤖 **LLM** pour générer une réponse contextualisée à partir des documents récupérés
- 🎛️ **Température** pour contrôler la créativité de la réponse générée (ex : 0.1 = réponse très précise, 1.0 = plus libre)

> 💡 *La température est un paramètre influençant le degré de "créativité" du modèle : plus elle est basse, plus les réponses sont déterministes. Une température de 0.7 est un bon équilibre pour un agent informatif comme un assistant de voyage.*



### objectif de agent.py

créer un chatbot local qui:
- charge un modèle LLM open-source depuis haggingface
- lit la clé API depuis un fichier .env
- fontionne dans le terminal
- répond à tes questions jusqu'à ce que tu tapes exit

---

## 💻 Technologies utilisées

- [Transformers (Hugging Face)](https://huggingface.co/docs/transformers)
- [Huggingface Hub](https://huggingface.co/docs/huggingface_hub)
- [FAISS (Facebook AI Similarity Search)](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io/)
- Python 3.10+
---

## 🚀 Lancer le projet

### 1. Cloner le projet (ou créer ton dossier)


```bash
git clone https://github.com/mon-utilisateur/mon_agent_llm.git
cd mon_agent_llm
```
pour créer le dossier : 

```bash
mkdir mon_agent_llm
cd mon_agent_llm
code . # ouvrir le dossier dans vscode
```
### 2. Créer un environnement virtuel 

```bash
python -m venv .venv
.venv\Scripts\activate # sous Windows
# ou source .venv/bin/activate  # sous Mac/Linux

```

### 3. Installer les dépendances 

pip install -r requirements.txt


### 4. Créer un compte hugging face et une clé

1. https://huggingface.co/join

2. Générez une clé ici : https://huggingface.co/settings/tokens

3. Permission : Read

### 5. ajouter la clé huggingface dans un fichier .env

HUGGINGFACEHUB_API_TOKEN=ta_clé_personnelle_ici


### 6. Lancer l'agent 
streamlit run agent.py


## Info utile:

## Pourquoi FAISS pour le RAG?

FAISS permet une recherche vectorielle rapide et efficace, en comparant les embeddings de la question de l’utilisateur avec ceux des documents de la base. C’est une solution adaptée pour les projets locaux sans backend complexe.


---

# 🇬🇧 English Version – `README.md`

```markdown
# 🧠 My LLM Agent (Free with Hugging Face + RAG)

This project is a **simple conversational agent** powered by an open-source LLM hosted on Hugging Face and enhanced with a local knowledge base using RAG (Retrieval-Augmented Generation).

---

## 🔧 Project Goals

Build a chatbot that:
- Uses an open-source LLM (e.g. `Mixtral-8x7B-Instruct` or `Mistral-7B-Instruct`)
- Runs for free via the Hugging Face Inference API
- Retrieves knowledge from a local text base (RAG)
- Can be used in the terminal or via a visual Streamlit interface
- Is easy to customize and extend

---

## 📚 How It Works

The agent combines:
- 🔍 **FAISS** for fast similarity search over a local database (Q/A pairs)
- 🤖 **LLM** to generate contextualized answers
- 🎛️ **Temperature** to control creativity level (0.1 = deterministic, 1.0 = creative)

> 💡 *Temperature controls how random or deterministic the model’s responses are. A value of 0.7 offers a good balance for informative assistants like a travel bot.*

---

## 📁 Project Structure

mon_agent_llm/
│
├── agent.py # CLI-based chatbot
├── app.py / test.py # Streamlit interface with RAG
├── base_base.txt # Local text knowledge base
├── .env # Hugging Face API token
├── requirements.txt # Python dependencies
└── README.md # This file 🧠


---

## 💻 Tech Stack

- [Transformers (Hugging Face)](https://huggingface.co/docs/transformers)
- [Huggingface Hub](https://huggingface.co/docs/huggingface_hub)
- [FAISS](https://github.com/facebookresearch/faiss)
- [Sentence Transformers](https://www.sbert.net/)
- [Streamlit](https://streamlit.io/)
- Python 3.10+

---

## 🚀 Run the Project

### 1. Clone the repo

```bash
git clone https://github.com/your-username/mon_agent_llm.git
cd mon_agent_llm

```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate  # On Windows
# Or source .venv/bin/activate  # On Mac/Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt

```

### 4. Create a Hugging Face account & token

    https://huggingface.co/join

    Generate a token: https://huggingface.co/settings/tokens

    Permission: Read

the create a .venv file and add:
```bash 
HF_TOKEN=hf_your_personal_token

```
### 5. Launch the agent 

```bash
Streamlit run agent.py
```