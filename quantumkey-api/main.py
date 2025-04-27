from fastapi import FastAPI

# Маршруты ядра
from app.threshold import router as threshold_router
from app.vdf import router as vdf_router
from app.pq_signature import router as pq_router

app = FastAPI(
    title="QuantumKey Vault API",
    version="0.2.0",
    description="API for QuantumKey Vault with Threshold Vaults, VDF, PQ-Signature and more"
)

# Подключаем маршруты
app.include_router(
    threshold_router,
    prefix="/threshold",
    tags=["Threshold Vaults"]
)

app.include_router(
    vdf_router,
    prefix="/vdf",
    tags=["Verifiable Delay Function"]
)

app.include_router(
    pq_router,
    prefix="/pq",
    tags=["PQ-Signature"]
)

@app.get("/", tags=["Root"])
async def read_root():
    """
    Документ:
    Приветственный эндпоинт.
    """
    return {"message": "Welcome to QuantumKey Vault API!"}
