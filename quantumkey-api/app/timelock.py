# quantumkey-api/app/timelock.py

import time
from uuid import uuid4
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# простые pydantic-модели для запросов/ответов
class CreateReq(BaseModel):
    message: str
    unlock_in: int

class OpenResp(BaseModel):
    message: str

# внутренняя in-memory «база»
_STORE: dict[str, dict] = {}

@router.post("/create")
async def create(req: CreateReq):
    lock_id = str(uuid4())
    _STORE[lock_id] = {
        "msg": req.message,
        "ts": time.time(),
        "unlock_in": req.unlock_in,
    }
    return {"id": lock_id}

@router.get("/open/{id_}", response_model=OpenResp)
async def open_lock(id_: str):
    rec = _STORE.get(id_)
    if not rec:
        raise HTTPException(status_code=404, detail="not found")
    if time.time() < rec["ts"] + rec["unlock_in"]:
        raise HTTPException(status_code=403, detail="not yet unlocked")
    return {"message": rec["msg"]}
