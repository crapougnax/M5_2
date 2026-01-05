import streamlit as st
import requests
from loguru import logger

# Configuration du logging
logger.add("frontend.log", rotation="1 MB")

st.title("FastIA - Calculateur de Carré")
st.write("Ce projet est un template d'architecture pour les projets IA de FastIA.")

# Input utilisateur
number = st.number_input("Entrez un nombre entier", value=0, step=1, format="%d")

if st.button("Calculer"):
    logger.info(f"Utilisateur a demandé le calcul pour : {number}")
    
    try:
        # Appel à l'API Backend
        # Note: Dans docker-compose, le service s'appellera 'backend'
        # Pour le dev local hors docker, on pourrait utiliser localhost
        # Ici on configure pour que ça marche avec docker-compose par défaut, ou on pourrait mettre une variable d'env
        api_url = "http://backend:8000/calculate" 
        
        payload = {"number": int(number)}
        response = requests.post(api_url, json=payload)
        
        if response.status_code == 200:
            result = response.json().get("result")
            st.success(f"Le carré de {number} est {result}")
            logger.info(f"Succès: {result}")
        else:
            st.error(f"Erreur API : {response.status_code}")
            logger.error(f"Erreur API : {response.text}")
            
    except requests.exceptions.ConnectionError:
        st.error("Impossible de contacter le backend. Vérifiez qu'il est lancé.")
        logger.error("Erreur de connexion au backend")
    except Exception as e:
        st.error(f"Erreur inattendue : {e}")
        logger.error(f"Erreur inattendue : {e}")
