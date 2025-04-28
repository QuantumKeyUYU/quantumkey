#!/usr/bin/env python3
# main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Импорт существующих модулей
from app.threshold_vault import router as threshold_router
from app.vdf import router as vdf_router
from app.timelock import router as timelock_router

# Новый PQ-Signature модуль
from app.pq_signature import router as pq_router

app = FastAPI(
    title="QuantumKey Vault API",
    version="0.1.0",
    description=(
        "QuantumKey Vault: надежное хранение секретов с модулями "
        "Threshold Vaults, VDF, TimeLock и PQ-Signature."
    ),
)

# Настройка CORS (для разработки открыто — в проде сужайте allow_origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Подключаем роутеры всех модулей
app.include_router(threshold_router)   # /threshold/*
app.include_router(vdf_router)         # /vdf/*
app.include_router(timelock_router)    # /timelock/*
app.include_router(pq_router)          # /pq/*

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
