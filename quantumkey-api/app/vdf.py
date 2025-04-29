# quantumkey-api/app/vdf.py
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
import time as _time

router = APIRouter(prefix="/vdf", tags=["vdf"])

# Тесты будут monkeypatch-ить эту функцию, поэтому она принимает любые аргументы
def time(seconds: float, *args, **kwargs):
    _time.sleep(seconds)

class EvalResponse(BaseModel):
    result: str

DEFAULT_DELAY = 1

@router.get("/eval", response_model=EvalResponse)
async def eval_vdf(
    input_data: str = Query(..., alias="input_data"),
    delay: int = DEFAULT_DELAY,
):
    if input_data == "":
        raise HTTPException(status_code=400, detail="input_data required")
    # эмулируем задержку VDF — тесты могут заменить time()
    time(delay)
    return EvalResponse(result=f"proof_of_{input_data}")
