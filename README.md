# 🧠 Assistant IA Métier – Architecture RAG (POC)

## 📌 Présentation du projet

Ce projet est un **Proof of Concept (POC)** d’un **assistant conversationnel intelligent** basé sur l’architecture **RAG (Retrieval-Augmented Generation)**.

L’objectif est de permettre aux collaborateurs d’interroger **la base de connaissances interne de l’entreprise** (procédures, guides, politiques RH, documents métiers) de manière :

* intuitive
* sécurisée
* fiable (sans hallucinations)

---

## ✨ Fonctionnalités principales

### 🔍 Recherche sémantique

* Compréhension du langage naturel
* Pas besoin de correspondance exacte de mots-clés

### 🧠 Maîtrise de l’information

* Les réponses sont **strictement limitées au contenu des documents fournis**
* Réduction drastique des risques d’hallucination du LLM

### 📚 Citations des sources

* Chaque réponse inclut :

  * le **document source**
  * le **numéro de page**

### ⬇️ Accès aux documents

* Téléchargement direct du document PDF depuis l’interface utilisateur

---

## 🏗️ Architecture technique

### 📄 Ingestion & préparation des documents

* Chargement des PDF via `PyPDFLoader`
* Découpage intelligent avec `RecursiveCharacterTextSplitter`

  * Taille des chunks : **1500 caractères**

### 🧩 Base vectorielle

* **ChromaDB** pour le stockage des embeddings
* Embeddings générés via **HuggingFace**

### 🤖 Modèle de langage (LLM)

* **Llama 3.1**
* Hébergé sur l’infrastructure **Groq Cloud**
* Génération rapide et performante

---

## ⚙️ Prérequis système

Avant de commencer, assurez-vous d’avoir :

* **Python 3.9** ou supérieur
* **Git**
* Un compte **Groq Cloud**
  👉 [https://console.groq.com/home](https://console.groq.com/home)

### 🔑 Variable d’environnement requise

```env
GROQ_API_KEY=votre_cle_api
```

---

## 🚀 Installation

### 1️⃣ Cloner le repository

```bash
git clone https://github.com/------/Assistant_IA.git
cd Assistant_IA
```

### 2️⃣ Créer et activer un environnement virtuel

```bash
python -m venv env
env\Scripts\activate   # Windows
# source env/bin/activate  # Linux / Mac
```

### 3️⃣ Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## 📁 Structure du projet

```plaintext
Assistant_IA/
├── app/                     # Interface utilisateur (Streamlit)
│   └── chat.py
│
├── chroma_db/               # Base vectorielle (générée automatiquement)
│
├── ingestion/               # Pipeline d’ingestion des documents
│   ├── __init__.py
│   ├── load_docs.py         # Chargement des PDF
│   ├── chunking.py          # Découpage du texte
│   └── embed_store.py       # Génération et stockage des embeddings
│
├── rag/                     # Logique RAG
│   ├── __init__.py
│   ├── retriever.py         # Recherche vectorielle
│   └── generator.py         # Génération de réponse (Groq API)
│
├── Data/
│   └── Documents/           # Sources PDF
│
├── .env                     # Variables d’environnement (non versionné)
├── .env.example             # Modèle de configuration
├── .gitignore
├── main.py                  # Chaîne complète d’ingestion
└── requirements.txt         # Dépendances Python
```

---

## 🧪 Génération de la base vectorielle

Après avoir ajouté vos documents PDF dans :

```plaintext
Data/Documents/
```

Lancez :

```bash
python main.py
```

Cela :

* charge les documents
* les découpe
* génère les embeddings
* les stocke dans ChromaDB

---

## ▶️ Lancer l’application

```bash
python -m streamlit run app/chat.py
```

L’interface Streamlit sera accessible depuis votre navigateur.

---

## 🛠️ Dépannage (FAQ)

### ❌ `ModuleNotFoundError`

* Vérifiez que l’environnement virtuel est bien activé
* Relancez :

```bash
pip install -r requirements.txt
```

### ❌ L’assistant ne trouve aucune source

* Vérifiez que des PDF sont bien présents dans `Data/Documents/`
* Relancez :

```bash
python main.py
```

### ❌ Erreur de clé API Groq

* Vérifiez que le fichier `.env` existe bien
* La clé doit commencer par : `gsk_`

---

## 📌 Notes

* Ce projet est un **POC** et peut être étendu :

  * authentification utilisateur
  * gestion des rôles
  * ajout d’autres formats de documents
  * déploiement cloud
