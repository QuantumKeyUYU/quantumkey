from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.pq_signature    import router as pq_router
from app.threshold_vault import router as threshold_router
from app.timelock        import router as timelock_router
from app.vdf             import router as vdf_router

app = FastAPI(
    title="QuantumKey Vault API",
    version="0.1.0",
    description="Stub API for PQ-signature, Threshold Vault, TimeLock and VDF endpoints"
)

# Разрешаем CORS со всех источников (для фронтенда)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры
app.include_router(pq_router,        prefix="/pq",        tags=["pq_signature"])
app.include_router(threshold_router, prefix="/threshold", tags=["threshold_vault"])
app.include_router(timelock_router,  prefix="/timelock",  tags=["timelock"])
app.include_router(vdf_router,       prefix="/vdf",       tags=["vdf"])
