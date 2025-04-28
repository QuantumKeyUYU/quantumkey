# quantumkey-api/main.py
from fastapi import FastAPI
from app.threshold     import router as threshold_router
from app.vdf           import router as vdf_router
from app.timelock      import router as timelock_router
from app.pq_signature  import router as pq_router

app = FastAPI(title="QuantumKey Vault API", version="0.3.0")

# Threshold
app.include_router(threshold_router, prefix="/threshold", tags=["Threshold"])
# VDF
app.include_router(vdf_router,       prefix="/vdf",       tags=["VDF"])
# TimeLock
app.include_router(timelock_router,  prefix="/timelock",  tags=["Timelock"])
# Post-Quantum Signature
app.include_router(pq_router,        prefix="/pq",        tags=["PQ-Signature"])
