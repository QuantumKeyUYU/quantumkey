from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.threshold_vault import router as threshold_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(threshold_router, prefix="/threshold", tags=["threshold_vault"])
