import time
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()
_store: dict[str, dict] = {}

class TimeLockCreateRequest(BaseModel):
    message: str
    unlock_in: int

class TimeLockCreateResponse(BaseModel):
    id: str

class TimeLockOpenResponse(BaseModel):
    message: str
    unlock_in: int

@router.post("/create", response_model=TimeLockCreateResponse)
async def create_timelock(req: TimeLockCreateRequest):
    id_ = "timelock_stub"
    _store[id_] = {
        "message": req.message,
        "unlock_in": req.unlock_in,
        "created": time.time(),
    }
    return {"id": id_}

@router.get("/open/{id}", response_model=TimeLockOpenResponse)
async def open_timelock(id: str):
    entry = _store.get(id)
    if entry is None:
        raise HTTPException(status_code=404, detail="Not found")
    if time.time() < entry["created"] + entry["unlock_in"]:
        raise HTTPException(status_code=403, detail="Forbidden")
    return {"message": entry["message"], "unlock_in": entry["unlock_in"]}
