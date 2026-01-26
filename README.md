Projet : Assistant IA Métier - (RAG )
Présentation du Projet
Ce projet présente un Proof of Concept (POC) d'un assistant conversationnel basé sur l'architecture RAG (Retrieval-Augmented Generation). L'objectif est de permettre aux collaborateurs d'interroger la base de connaissances interne de l'entreprise (procédures, guides, politiques RH) de manière intuitive et sécurisée.

Fonctionnalités Principales
Recherche Sémantique : Compréhension du langage naturel pour extraire des informations sans correspondance exacte des mots-clés.

Maîtrise de l'Information : Réponses limitées strictement au contexte des documents fournis pour éliminer les risques d'hallucination.

Citations des Sources : Pour chaque réponse, l'assistant indique le document source et le numéro de page correspondant.

Accessibilité : Possibilité de télécharger le document original directement depuis l'interface.

Architecture Technique
Extraction et Découpage : Utilisation de PyPDFLoader et RecursiveCharacterTextSplitter (chunks de 1500 caractères).

Base Vectorielle : ChromaDB pour le stockage des embeddings générés par HuggingFace.

Modèle de Langage (LLM) : Llama 3.1 hébergé sur l'infrastructure Groq pour une génération haute performance.

Prérequis Système
Avant de commencer, assurez-vous d'avoir installé :

Python 3.9 ou une version supérieure.
Git (pour cloner le projet).
Un compte sur Groq Cloud pour obtenir une clé API.https://console.groq.com/home
GROQ_API_KEY=votre_cle_api


Cloner le repository :
git clone https://github.com/------/Assistant_IA.git
cd Assistant_IA

Créer un environnement virtuel :
python -m venv env
env\Scripts\activate

Installation des dépendances :
pip install -r requirements.txt


Structure du Répertoire
plaintext
Assistant_IA/
├── app/                   # Interface utilisateur Streamlit
│   └── chat.py
├── chroma_db/             # Base de données vectorielle (générée)    
├── ingestion/             # Nouveau package d'ingestion
│   ├── __init__.py
│   ├── embed_store.py      # Création des vecteurs et stockage  
│   ├── chunking.py         # Découpage du texte
│   └── load_docs.py        # Chargement des PDF        # Interface utilisateur (Streamlit)
├── rag/
    ├── __init__.py
│   ├── retriever.py       # Moteur de recherche vectorielle
│   └── generator.py       # Logique de génération (Groq API)
├── Data/
│   └── Documents/         # Sources PDF
├── .env                   
├── .gitignore/
│   └── .env               # Exclusion des fichiers sensibles          
├── .env.example           # Modèle de configuration des clés API
├── main.py                #Chaîne de Traitement des Données
└── requirements.txt       # Dépendances Python

Lancer  la génération de la base vectorielle :
python main.py

Exécution :
python -m streamlit run app/chat.py


Dépannage (FAQ)
Erreur ModuleNotFoundError : Vérifiez que vous avez bien activé l'environnement virtuel et lancé pip install.

L'assistant dit qu'il ne trouve pas de source : Assurez-vous d'avoir lancé python ingestion/embed_store.py après avoir ajouté des PDF dans le dossier Data/Documents/.

Erreur de clé API : Vérifiez que le fichier .env est correctement nommé et que la clé Groq commence bien par gsk_.

