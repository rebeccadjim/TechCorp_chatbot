import streamlit_authenticator as stauth
hashed = stauth.Hasher.hash("votre_mot_de_passe")
print(hashed)