from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from loguru import logger
from backend.modules.calcul import carre

app = FastAPI(title="FastIA API", description="API pour le calcul de carrés", version="1.0.0")

# Modèles Pydantic
class NumberInput(BaseModel):
    number: int

class NumberOutput(BaseModel):
    result: int

@app.get("/")
async def root():
    logger.info("Accès à la racine")
    return {"message": "Bienvenue sur l'API FastIA"}

@app.get("/health")
async def health_check():
    logger.info("Vérification de l'état de santé")
    return {"status": "ok"}

@app.post("/calculate", response_model=NumberOutput)
async def calculate(input_data: NumberInput):
    logger.info(f"Demande de calcul pour : {input_data.number}")
    try:
        res = carre(input_data.number)
        logger.info(f"Résultat calculé : {res}")
        return {"result": res}
    except Exception as e:
        logger.error(f"Erreur lors du calcul : {e}")
        raise HTTPException(status_code=500, detail=str(e))
