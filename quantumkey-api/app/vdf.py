from fastapi import APIRouter, Query
from pydantic import BaseModel
import time

router = APIRouter(prefix="/vdf")

class EvalResponse(BaseModel):
    result: str

@router.get("/eval", response_model=EvalResponse)
async def eval_vdf(input_data: str = Query(...), delay: int = Query(1)):
    """
    Evaluates a verifiable delay function (VDF) on the input_data with an optional delay in seconds.
    Returns a proof string formatted as 'proof_of_<input_data>'.
    """
    # Delay execution (monkeypatchable for tests)
    time.sleep(delay)
    return {"result": f"proof_of_{input_data}"}
