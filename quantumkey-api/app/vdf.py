import time
from fastapi import APIRouter, HTTPException
from fastapi.params import Query
from pydantic import BaseModel

DEFAULT_DELAY = 2

router = APIRouter()

class EvalResponse(BaseModel):
    result: str

@router.get("/eval", response_model=EvalResponse)
async def eval_vdf(
    input_data: str = Query(..., alias="input_data"),
    delay: int   = Query(DEFAULT_DELAY),
):
    if input_data == "":
        raise HTTPException(status_code=400, detail="input_data required")

    time.sleep(delay)
    return {"result": f"proof_of_{input_data}"}
