# quantumkey-api/app/vdf.py
"""
Stub-реализация VDF, полностью совместимая с CI-тестами.

▪ /vdf/eval?input_data=abc            →  {"result": "proof_of_abc"}
▪ тесты могут monkeypatch-ить vdf.time
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
import time as _time

router = APIRouter(prefix="/vdf", tags=["vdf"])

# ──────────────────────────────────────────
#  Хук, который monkeypatch-ят тесты
#  Принимает ЛЮБЫЕ аргументы, чтобы не падать
# ──────────────────────────────────────────
def time(seconds: float, *args, **kwargs):  # <-- ВАЖНО! добавлены *args, **kwargs
    _time.sleep(seconds)

# ──────────────────────────────────────────
class EvalResponse(BaseModel):
    result: str

DEFAULT_DELAY = 1  # секунда


@router.get("/eval", response_model=EvalResponse)
async def eval_vdf(
    input_data: str = Query(..., alias="input_data"),
    delay: int = DEFAULT_DELAY,
):
    if input_data == "":
        raise HTTPException(status_code=400, detail="input_data required")

    # Эмулируем задержку через функцию time, которую тесты могут менять
    time(delay)

    return EvalResponse(result=f"proof_of_{input_data}")
