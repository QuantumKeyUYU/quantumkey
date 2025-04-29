from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import time
from uuid import uuid4

router = APIRouter(prefix="/timelock", tags=["timelock"])
_STORE: dict[str, dict] = {}

class CreateReq(BaseModel):
    message: str
    unlock_in: int

class OpenResp(BaseModel):
    message: str

@router.post("/create")
async def create(req: CreateReq):
    lock_id = str(uuid4())
    _STORE[lock_id] = {
        "msg": req.message,
        "ts": time.time() + req.unlock_in
    }
    return {"id": lock_id}

@router.get("/open/{lock_id}", response_model=OpenResp)
async def open_lock(lock_id: str):
    entry = _STORE.get(lock_id)
    if not entry:
        raise HTTPException(status_code=404, detail="not found")
    if time.time() < entry["ts"]:
        raise HTTPException(status_code=403, detail="forbidden")
    return {"message": entry["msg"]}
