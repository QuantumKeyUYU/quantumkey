# quantumkey-api/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import threshold_vault
from app import vdf
from app import timelock
from app import pq_signature

app = FastAPI(
    title="QuantumKey Vault API",
    version="0.3.0",
    description="Secure secret storage: Threshold, VDF, TimeLock & PQ-Signature"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Регистрируем все роутеры
app.include_router(threshold_vault.router)
app.include_router(vdf.router)
app.include_router(timelock.router)
app.include_router(pq_signature.router)
