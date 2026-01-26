import os
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader, TextLoader

def load_professional_docs(directory_path):
    print(f"--- Étape 1 : Chargement des documents dans {directory_path} ---")
    
    # Chargement des PDF
    pdf_loader = DirectoryLoader(directory_path, glob="*.pdf", loader_cls=PyPDFLoader)
    pdf_docs = pdf_loader.load()
    
    # --- MODIFICATION ICI : On ajoute loader_kwargs pour forcer l'UTF-8 ---
    txt_loader = DirectoryLoader(
        directory_path, 
        glob="*.txt", 
        loader_cls=TextLoader,
        loader_kwargs={'encoding': 'utf-8'} # <--- C'est cette ligne qui sauve ton projet
    )
    txt_docs = txt_loader.load()
    
    docs = pdf_docs + txt_docs
    
    # Nettoyage simple
    for doc in docs:
        doc.page_content = doc.page_content.replace('\n', ' ').strip()
        
    print(f" {len(docs)} documents chargés au total.")
    return docs