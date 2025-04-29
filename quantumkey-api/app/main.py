from fastapi import FastAPI
from app.threshold_vault import router as threshold_router
from app.vdf            import router as vdf_router
from app.timelock       import router as timelock_router
from app.pq_signature   import router as pq_router

app = FastAPI(title="QuantumKey Vault API")

# подтягиваем все роутеры
app.include_router(threshold_router)
app.include_router(vdf_router)
app.include_router(timelock_router)
app.include_router(pq_router)
