# quantumkey-api/main.py
"""
Главный файл FastAPI-приложения QuantumKey Vault.

Подключает все текущие модули:
• Threshold Vaults   – /threshold/*
• VDF (Eval)        – /vdf/*
• TimeLock          – /timelock/*
• PQ-Signature      – /pq/*
При добавлении новых пакетов (TEE, Bio и т.д.) просто импортируйте
router и добавьте app.include_router(<router>).
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# ▸ Импорт роутеров модулей
from app import threshold_vault       as threshold
from app import vdf                   as vdf
from app import timelock              as timelock
from app import pq_signature          as pq_signature
# (дальше будут: tee, bio, zk, …)

app = FastAPI(
    title="QuantumKey Vault API",
    version="0.3.0",
    description=(
        "Secure secret-management platform: Threshold Vaults, "
        "VDF, TimeLock and PQ-Signatures."
    ),
)

# ─────────────────────────────────────────────────────────────
#  CORS — на время разработки открыт для любых источников
#  В production сузьте allow_origins!
# ─────────────────────────────────────────────────────────────
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ─────────────────────────────────────────────────────────────
#  Регистрация роутеров
# ─────────────────────────────────────────────────────────────
app.include_router(threshold.router)    # /threshold/*
app.include_router(vdf.router)          # /vdf/*
app.include_router(timelock.router)     # /timelock/*
app.include_router(pq_signature.router) # /pq/*

# ─────────────────────────────────────────────────────────────
#  Локальный запуск:  python -m uvicorn app.main:app --reload
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
