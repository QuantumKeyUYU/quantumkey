from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
import asyncio

router = APIRouter(prefix="/vdf", tags=["vdf"])
DEFAULT_DELAY = 3

class EvalResponse(BaseModel):
    result: str

@router.get("/eval", response_model=EvalResponse)
async def eval_vdf(input_data: str, delay: Optional[int] = DEFAULT_DELAY):
    if input_data == "":
        raise HTTPException(status_code=400, detail="input_data required")
    # «симуляция» задержки
    await asyncio.sleep(delay)
    return {"result": f"proof_of_{input_data}"}
