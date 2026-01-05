# FastIA Project Template

Ce dépôt contient un template d'architecture minimaliste et extensible pour les projets d'Intelligence Artificielle de FastIA. Il vise à séparer clairement le frontend du backend, à conteneuriser l'environnement et à automatiser les tests via l'intégration continue.

## 🏗 Architecture

Le projet est composé de deux services principaux orchestrés par Docker Compose :

- **Frontend** (`frontend/`) : Une interface utilisateur réalisée avec **Streamlit**. Elle permet de saisir un nombre entier et affiche le résultat du calcul.
- **Backend** (`backend/`) : Une API REST réalisée avec **FastAPI**. Elle expose un endpoint `/calculate` qui valide l'entrée et retourne le carré de l'entier.
- **Logique Métier** (`backend/modules/calcul.py`) : Un module dédié contenant la logique de calcul, isolé de la couche API.

## 🛠 Technologies

- **Frontend** : Streamlit
- **Backend** : FastAPI, Pydantic, Uvicorn
- **Conteneurisation** : Docker, Docker Compose
- **Logs** : Loguru
- **Tests** : Pytest
- **CI/CD** : GitHub Actions

## 🚀 Installation et Lancement

### Prérequis

- Docker
- Docker Compose

### Lancement Rapide

Pour lancer l'application complète (frontend + backend) :

```bash
docker-compose up --build
```

L'application sera accessible aux adresses suivantes :

- **Frontend** : http://localhost:8501
- **API Docs (Swagger UI)** : http://localhost:8000/docs

## 📁 Structure du Projet

```
.
├── backend/
│   ├── Dockerfile          # Image Docker du backend
│   ├── main.py             # Point d'entrée de l'API FastAPI
│   ├── modules/
│   │   └── calcul.py       # Logique métier pur
│   ├── tests/
│   │   └── test_calcul.py  # Tests unitaires
│   └── requirements.txt    # Dépendances Python backend
├── frontend/
│   ├── Dockerfile          # Image Docker du frontend
│   ├── app.py              # Application Streamlit
│   └── requirements.txt    # Dépendances Python frontend
├── .github/
│   └── workflows/
│       └── ci.yml          # Pipeline d'intégration continue
├── docker-compose.yml      # Orchestration des conteneurs
└── README.md
```

## ✅ Intégration Continue (CI)

Un workflow GitHub Actions est configuré dans `.github/workflows/ci.yml`. À chaque `push` ou `pull_request` sur la branche `main` :

1.  L'environnement Python est configuré.
2.  Les dépendances backend sont installées.
3.  Les tests unitaires (`pytest`) sont exécutés pour valider la logique métier.

## 🧪 Tests Locaux

Pour exécuter les tests du backend localement sans Docker :

```bash
# Créer un environnement virtuel (optionnel mais recommandé)
python -m venv .venv
source .venv/bin/activate

# Installer les dépendances
pip install -r backend/requirements.txt

# Lancer les tests
PYTHONPATH=. pytest backend/tests/
```
