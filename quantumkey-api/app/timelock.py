# quantumkey-api/app/timelock.py

import time
from uuid import uuid4

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Простое in-memory хранилище замков
_STORE: dict[str, dict] = {}

class CreateReq(BaseModel):
    message: str
    unlock_in: int  # секунд до открытия

class CreateRes(BaseModel):
    id: str

@router.post("/create", response_model=CreateRes)
async def create(req: CreateReq):
    lock_id = str(uuid4())
    _STORE[lock_id] = {
        "msg": req.message,
        "ts": time.time() + req.unlock_in,
    }
    return {"id": lock_id}

@router.get("/open/{lock_id}")
async def open_lock(lock_id: str):
    rec = _STORE.get(lock_id)
    if rec is None:
        # нет такого lock_id
        raise HTTPException(status_code=404, detail="Not found")
    if time.time() < rec["ts"]:
        # ещё рано
        raise HTTPException(status_code=403, detail="Forbidden")
    # возвращаем сообщение
    return {"message": rec["msg"]}
