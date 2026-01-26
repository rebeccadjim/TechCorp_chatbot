import streamlit as st
import os
from dotenv import load_dotenv 
from rag.retriever import get_relevant_chunks
from rag.generator import generate_answer

# --- CHARGEMENT DE LA CLÉ API ---
load_dotenv()

# Configuration de la page
st.set_page_config(page_title="🤖 Assistant RH TechCorp", page_icon="🤖")

st.title(" 🤖 Assistant RH TechCorp")
st.markdown("Bienvenue, comment puis-je vous aider aujourd'hui ?")

# Initialisation de l'historique
if "messages" not in st.session_state:
    st.session_state.messages = []

# Affichage des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Zone de saisie
if prompt := st.chat_input("Votre message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        with st.spinner("Recherche dans la base de connaissances..."):
            try:
                # 1. Recherche des morceaux (chunks)
                chunks = get_relevant_chunks(prompt)
                
                # 2. Génération de la réponse
                reponse = generate_answer(prompt, chunks)
                st.markdown(reponse)
                
                # --- 3. AFFICHAGE CONDITIONNEL DES SOURCES ---
                mots_cles_refus = ["désolé", "ne sais pas", "pas trouvé", "pas de mention", "aucun document"]
                
                if not any(mot in reponse.lower() for mot in mots_cles_refus):
                    if chunks:
                        with st.expander("📄 Vérifier les sources et télécharger les documents"):
                            st.write("Documents utilisés pour cette réponse :")
                            
                            for i, doc in enumerate(chunks):
                                file_path = doc.metadata.get('source')
                                if file_path and os.path.exists(file_path):
                                    nom_fichier = os.path.basename(file_path)
                                    page = doc.metadata.get('page', '?')
                                    
                                    # Détection dynamique du type de fichier
                                    extension = os.path.splitext(nom_fichier)[1].lower()
                                    type_mime = "application/pdf" if extension == ".pdf" else "text/plain"

                                    st.info(f"**Source {i+1}:** {nom_fichier} (Page {page})")
                                    st.caption(f"Extrait : {doc.page_content[:150]}...")

                                    with open(file_path, "rb") as f:
                                        st.download_button(
                                            label=f"📥 Télécharger {nom_fichier}",
                                            data=f,
                                            file_name=nom_fichier,
                                            mime=type_mime,
                                            key=f"dl_{i}_{nom_fichier}"
                                        )
                                    st.divider()
                else:
                    st.warning("⚠️ Aucune source officielle n'a été trouvée pour cette demande.")

            except Exception as e:
                st.error(f"Erreur technique : {e}")
                reponse = "Désolé, une erreur est survenue."
        
    st.session_state.messages.append({"role": "assistant", "content": reponse})