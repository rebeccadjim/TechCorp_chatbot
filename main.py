import os
from ingestion.load_docs import load_professional_docs
from ingestion.chunking import split_documents
from ingestion.embed_store import create_and_save_store

# Chemins
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PATH_DOCS = os.path.join(BASE_DIR, "Data", "Documents")
PATH_CHROMA = os.path.join(BASE_DIR, "chroma_db")

def run_ingestion():
    # Exécution de la chaîne complète
    docs = load_professional_docs(PATH_DOCS)
    
    if docs:
        chunks = split_documents(docs)
        create_and_save_store(chunks, PATH_CHROMA)
        print("\n INGESTION TERMINÉE AVEC SUCCÈS !")

if __name__ == "__main__":
    run_ingestion()