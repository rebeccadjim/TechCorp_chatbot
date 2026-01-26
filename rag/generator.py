import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage, SystemMessage

# Charge les variables du fichier .env
load_dotenv()

def generate_answer(question, context_chunks):
    # On récupère la clé explicitement pour éviter l'erreur technique
    api_key = os.getenv("GROQ_API_KEY")
    
    if not api_key:
        raise ValueError("ERREUR : La variable GROQ_API_KEY n'est pas définie dans le fichier .env")

    # Initialisation avec la clé
    llm = ChatGroq(
        model_name="llama-3.1-8b-instant", 
        temperature=0,
        groq_api_key=api_key
    )
    
    context_text = "\n\n".join([doc.page_content for doc in context_chunks])
    
    system_prompt = (
        "Tu es l'assistant strictement limité aux documents de TechCorp. "
        f"CONTEXTE FOURNI : \n{context_text}\n\n"
        "CONSIGNE : Réponds à la question en utilisant EXCLUSIVEMENT le contexte ci-dessus. "
        "Si la réponse n'est pas dans le texte, réponds que tu ne sais pas."
    )
    
    user_content = f"QUESTION DU COLLABORATEUR : {question}"
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_content)
    ]
    
    response = llm.invoke(messages)
    return response.content