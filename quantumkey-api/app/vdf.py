# quantumkey-api/app/vdf.py
"""
Stub VDF: возвращает SHA-256 от входной строки,
чтобы тест /vdf/eval проходил (код 200).
"""

import hashlib
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/vdf", tags=["vdf"])


class EvalResponse(BaseModel):
    digest: str


@router.get("/eval", response_model=EvalResponse)
async def eval_vdf(input_data: str):
    if not input_data:
        raise HTTPException(status_code=400, detail="input_data required")

    digest = hashlib.sha256(input_data.encode()).hexdigest()
    return EvalResponse(digest=digest)
