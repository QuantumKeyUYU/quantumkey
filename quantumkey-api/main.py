# quantumkey-api/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Импорт роутеров из модуля app
from app.threshold_vault import router as threshold_router
from app.vdf             import router as vdf_router
from app.timelock        import router as timelock_router
from app.pq_signature    import router as pq_router

app = FastAPI(
    title="QuantumKey Vault API",
    version="0.3.1",
    description="Secure key management: Threshold Vaults, VDF, TimeLock & PQ-Signatures"
)

# CORS-настройки (на время разработки можно открыть для всех)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Регистрируем эндпоинты
app.include_router(threshold_router)
app.include_router(vdf_router)
app.include_router(timelock_router)
app.include_router(pq_router)


# Точка входа для локального запуска через `python main.py`
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
