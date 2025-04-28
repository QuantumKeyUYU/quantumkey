from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app import threshold
from app import vdf
from app import timelock
from app import pq_signature

app = FastAPI(
    title="QuantumKey Vault API",
    version="0.3.0",
    description="Secure secret storage with Threshold Vaults, VDF, TimeLock and PQ Signatures",
    openapi_tags=[
        {"name": "Threshold", "description": "Split & Recover Secret using Threshold scheme"},
        {"name": "VDF", "description": "Evaluate Verifiable Delay Function (VDF)"},
        {"name": "Timelock", "description": "Create and Open Timelock encrypted secrets"},
        {"name": "PQ-signature", "description": "Post-Quantum Hybrid Signature (Falcon + VDF-proof)"},
    ]
)

# CORS Middleware (можно оставить открытым на время разработки)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры всех модулей
app.include_router(threshold.router)
app.include_router(vdf.router)
app.include_router(timelock.router)
app.include_router(pq_signature.router)
