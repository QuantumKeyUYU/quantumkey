# quantumkey-api/app/timelock.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime, timedelta, timezone
import uuid

router = APIRouter(prefix="/timelock", tags=["timelock"])

_store: dict[str, dict] = {}

class TimelockCreateRequest(BaseModel):
    message: str = Field(..., example="secret")
    unlock_in: int = Field(..., gt=0, description="seconds to wait")

class TimelockCreateResponse(BaseModel):
    id: str
    ready_at: datetime

class TimelockOpenResponse(BaseModel):
    message: str

@router.post("/create", response_model=TimelockCreateResponse)
async def create_timelock(req: TimelockCreateRequest):
    lock_id = str(uuid.uuid4())
    ready_at = datetime.now(timezone.utc) + timedelta(seconds=req.unlock_in)
    _store[lock_id] = {"message": req.message, "ready_at": ready_at}
    return TimelockCreateResponse(id=lock_id, ready_at=ready_at)

@router.get("/open/{lock_id}", response_model=TimelockOpenResponse)
async def open_timelock(lock_id: str):
    entry = _store.get(lock_id)
    if entry is None:
        raise HTTPException(status_code=404, detail="Timelock ID not found")
    if datetime.now(timezone.utc) < entry["ready_at"]:
        raise HTTPException(status_code=403, detail="Timelock not ready")
    return TimelockOpenResponse(message=entry["message"])
