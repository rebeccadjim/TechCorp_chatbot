import os
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def get_relevant_chunks(query):
    # --- SOLUTION : CHEMIN RELATIF ---
    # On récupère le dossier où se trouve le projet actuel
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # On pointe vers le dossier chroma_db à la racine du projet
    chemin_chroma = os.path.join(BASE_DIR, "chroma_db")
    
    # Configuration du modèle de recherche 
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    try:
        # On se connecte à la base ChromaDB
        vectorstore = Chroma(
            persist_directory=chemin_chroma, 
            embedding_function=embeddings
        )
        
        # k=5 : on récupère les 5 meilleurs extraits
        search_results = vectorstore.similarity_search(query, k=5)
        
        return search_results
        
    except Exception as e:
        print(f"Erreur lors de la récupération dans la base : {e}")
        return []