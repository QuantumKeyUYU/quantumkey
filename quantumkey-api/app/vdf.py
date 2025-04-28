# quantumkey-api/app/vdf.py
"""
VDF-заглушка: эмулирует «доказательство задержки».
Алгоритм для CI-тестов:
    GET /vdf/eval?input_data=abc
→ 200 JSON  {"result": "proof_of_abc"}
Любая строка → "proof_of_<строка>"
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel

router = APIRouter(prefix="/vdf", tags=["vdf"])


class EvalResponse(BaseModel):
    result: str


@router.get("/eval", response_model=EvalResponse)
async def eval_vdf(input_data: str = Query(..., alias="input_data")):
    if not input_data:
        raise HTTPException(status_code=400, detail="input_data required")

    return EvalResponse(result=f"proof_of_{input_data}")
