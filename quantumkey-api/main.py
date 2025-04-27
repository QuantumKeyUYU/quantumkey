# quantumkey-api/main.py

from fastapi import FastAPI
from app.threshold import router as threshold_router
from app.vdf import router as vdf_router
from app.pq_signature import router as pq_router
from app.timelock import router as timelock_router

app = FastAPI(
    title="QuantumKey Vault API",
    version="0.2.0",
    description="Secure key management with Threshold Vaults, VDF, PQ-Signatures and TimeLock",
    openapi_url="/openapi.json",
)

# Threshold Vaults (SSS)
app.include_router(threshold_router, tags=["Threshold Vaults"])

# Verifiable Delay Function
app.include_router(vdf_router, tags=["Verifiable Delay Function"])

# PQ-Signature stub
app.include_router(pq_router, tags=["PQ-Signature"])

# QuantumTimeLock (timelock)
app.include_router(timelock_router, tags=["Quantum TimeLock"])


@app.get("/", summary="Health check / Root")
async def read_root():
    return {
        "status": "ok",
        "service": "QuantumKey Vault API",
        "version": app.version,
    }
