# quantumkey-api/app/timelock.py
"""
In-memory stub implementation of TimeLock.

— /timelock/create  – создаёт запись, возвращает ID и время готовности
— /timelock/open/{id} – если ready_at уже прошло → 200 + message,
                        иначе → 403 (не готово),
                        если id не найден → 404
"""

from datetime import datetime, timedelta, timezone
import uuid
from typing import Dict

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

router = APIRouter(prefix="/timelock", tags=["timelock"])

# ────────────────────────────
# 🗄   In-memory storage
# ────────────────────────────
_store: Dict[str, dict] = {}

# ────────────────────────────
# 📜   Schemas
# ────────────────────────────
class TimelockCreateRequest(BaseModel):
    message: str = Field(..., example="secret text")
    unlock_in: int = Field(..., ge=1, description="Seconds until message can be opened")

class TimelockCreateResponse(BaseModel):
    id: str
    ready_at: datetime

class TimelockOpenResponse(BaseModel):
    message: str

# ────────────────────────────
# 🚀   End-points
# ────────────────────────────
@router.post("/create", response_model=TimelockCreateResponse)
async def create_timelock(req: TimelockCreateRequest):
    lock_id = str(uuid.uuid4())
    ready_at = datetime.now(timezone.utc) + timedelta(seconds=req.unlock_in)

    _store[lock_id] = {
        "message": req.message,
        "ready_at": ready_at,
    }
    return TimelockCreateResponse(id=lock_id, ready_at=ready_at)


@router.get("/open/{lock_id}", response_model=TimelockOpenResponse)
async def open_timelock(lock_id: str):
    entry = _store.get(lock_id)
    if entry is None:
        raise HTTPException(status_code=404, detail="Timelock ID not found")

    if datetime.now(timezone.utc) < entry["ready_at"]:
        raise HTTPException(status_code=403, detail="Timelock not ready")

    return TimelockOpenResponse(message=entry["message"])
