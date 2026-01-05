FROM python:3.9-slim

WORKDIR /app

# Installation des dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt



# Exposition du port
EXPOSE 8000

# Création du package backend pour respecter les imports
# On copie tout le contenu du contexte (dossier backend local) dans /app/backend
COPY . backend/
ENV PYTHONPATH=/app

# Commande de lancement
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
