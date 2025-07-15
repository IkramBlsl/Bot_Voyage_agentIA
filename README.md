# 🧠 Mon Agent LLM (gratuit avec Hugging Face)

Ce projet est un **agent conversationnel simple**, construit à partir d’un modèle LLM open-source hébergé sur Hugging Face.

---

## 🔧 Objectif du projet

Créer un chatbot local qui :
- Utilise un modèle open-source (ex: Mistral-7B-Instruct)
- Fonctionne gratuitement grâce à Hugging Face
- Peut être lancé en ligne de commande
- Est facile à personnaliser

---

### objectif de agent.py

créer un chatbot local qui:
- charge un modèle LLM open-source depuis haggingface
- lit la clé API depuis un fichier .env
- fontionne dans le terminal
- répond à tes questions jusqu'à ce que tu tapes exit

## 📁 Structure du projet

mon_agent_llm/
│
├── agent.py # Script principal du chatbot
├── .env # Contient la clé API Hugging Face
├── requirements.txt # Dépendances du projet
└── README.md # Documentation du projet (toi ici 🧠)



---

## 💻 Technologies utilisées

- [Transformers](https://huggingface.co/docs/transformers)
- [Huggingface Hub](https://huggingface.co/docs/huggingface_hub)
- [Python dotenv](https://pypi.org/project/python-dotenv/)
- Python 3.10+ (testé avec X.X)

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
code . ## ouvrir le dossier dans vscode
```
### 2. Créer un environnement virtuel 

python -m venv .venv
.venv\Scripts\activate # ou source .venv/bin/activate sous Mac/Linux 


### 3. Installer les dépendances 
pip install -r requirements.txt

-- ou taper la commande suivante : pip install transformers huggingface_hub python-dotenv

### 4. Créer un compte hugging face et une clé
1. Aller sur https://huggingface.co/join
2. Créer un compte
3. Une fois connecté, il faut aller sur https://huggingface.co/settings/tokens
4. Cliquer sur "New token":
    - il faut lui donner un nom (ex: agent-test)
    - choisis Read comme permission 
    - Cliques sur create et copie la clé générée (commence par hf_...)


### 4. ajouter la clé huggingface dans un fichier .env
HUGGINGFACEHUB_API_TOKEN=ta_clé_personnelle_ici


### 5. Lancer l'agent 
python agent.py