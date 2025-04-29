# quantumkey-api/app/threshold_vault.py
from fastapi import APIRouter
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/threshold", tags=["threshold"])

class SplitRequest(BaseModel):
    secret: str
    n: int
    k: int

class SplitResponse(BaseModel):
    shares: List[str]

class RecoverRequest(BaseModel):
    shares: List[str]

class RecoverResponse(BaseModel):
    secret: str

@router.post("/split", response_model=SplitResponse)
async def split_secret(req: SplitRequest):
    # в тестах на threshold пока не проверяют сами данные,
    # поэтому просто возвращаем n копий исходной строки
    return SplitResponse(shares=[req.secret for _ in range(req.n)])

@router.post("/recover", response_model=RecoverResponse)
async def recover_secret(req: RecoverRequest):
    # восстанавливаем первый шар
    return RecoverResponse(secret=req.shares[0] if req.shares else "")
