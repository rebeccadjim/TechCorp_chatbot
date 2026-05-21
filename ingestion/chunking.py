from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    print("--- Étape 2 : Découpage des documents (Chunking) ---")
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1500, # Ta valeur optimisée
        chunk_overlap=400,
        separators=["\n\n", "\n", ".", " ", ""]
    )
    
    chunks = text_splitter.split_documents(documents)
    print(f" {len(chunks)} morceaux créés.")
    return chunks