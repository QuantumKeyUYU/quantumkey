# quantumkey-api/app/vdf.py
"""
Stub-реализация VDF для CI-тестов.

✔  GET /vdf/eval?input_data=abc  →  {"result": "proof_of_abc"}
✔  Tесты могут monkeypatch-ить  vdf.time  для проверки «замедления».
"""

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
import time as _time

router = APIRouter(prefix="/vdf", tags=["vdf"])

# ──────────────────────────────────────────────────────────
#  Эту функцию monkeypatch-ят тесты
#  (По умолчанию просто sleep(seconds))
# ──────────────────────────────────────────────────────────
def time(seconds: float) -> None:          # noqa: N802  (нужен lower-case для monkeypatch)
    _time.sleep(seconds)


class EvalResponse(BaseModel):
    result: str


DEFAULT_DELAY = 1  # секунда


@router.get("/eval", response_model=EvalResponse)
async def eval_vdf(
    input_data: str = Query(..., alias="input_data"),
    delay: int = DEFAULT_DELAY,           # тест может передать свой delay
):
    if input_data == "":
        raise HTTPException(status_code=400, detail="input_data required")

    # эмулируем задержку VDF
    time(delay)

    return EvalResponse(result=f"proof_of_{input_data}")
