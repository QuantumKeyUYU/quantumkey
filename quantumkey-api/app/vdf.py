# quantumkey-api/app/vdf.py
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class EvalResponse(BaseModel):
    result: str

@router.get("/eval", response_model=EvalResponse)
def eval_vdf(input_data: str, delay: int = 5):
    import time
    time.sleep(delay)
    return {"result": f"proof_of_{input_data}"}
