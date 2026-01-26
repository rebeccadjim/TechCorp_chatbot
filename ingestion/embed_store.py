import os
import shutil
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

def create_and_save_store(chunks, path_chroma):
    print("--- Étape 3 : Création des vecteurs et stockage ---")
    
    # Nettoyage de l'ancienne base pour éviter les doublons
    if os.path.exists(path_chroma):
        shutil.rmtree(path_chroma)
    
    # Modèle d'embeddings gratuit et performant
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    
    # Création de la base Chroma
    vectorstore = Chroma.from_documents(
        documents=chunks, 
        embedding=embeddings, 
        persist_directory=path_chroma
    )
    
    print(f" Base vectorielle sauvegardée dans : {path_chroma}")
    return vectorstore