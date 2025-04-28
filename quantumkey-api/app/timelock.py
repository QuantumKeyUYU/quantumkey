# app/timelock.py

import os
import json
import uuid
from datetime import datetime, timedelta

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

# ⬇️ Попытка подключить Redis, если в окружении есть REDIS_URL
REDIS_URL = os.getenv("REDIS_URL")
if REDIS_URL:
    from redis.asyncio import Redis
    _redis = Redis.from_url(REDIS_URL, decode_responses=True)

    async def store_set(key: str, record: dict, ttl: int):
        # сохраняем JSON со сроком жизни ttl
        await _redis.set(key, json.dumps(record), ex=ttl + 60)

    async def store_get(key: str) -> dict | None:
        raw = await _redis.get(key)
        return json.loads(raw) if raw is not None else None

    async def store_delete(key: str):
        await _redis.delete(key)

else:
    # Простое in-memory хранилище (для тестов и CI)
    _store: dict[str, dict] = {}

    async def store_set(key: str, record: dict, ttl: int):
        _store[key] = record
        # TTL-автоочистку пока не делаем — записи убираются при open()

    async def store_get(key: str) -> dict | None:
        return _store.get(key)

    async def store_delete(key: str):
        _store.pop(key, None)


class TimelockCreate(BaseModel):
    message: str
    unlock_in: int  # секунды


router = APIRouter()


@router.post("/timelock/create")
async def create_timelock(req: TimelockCreate):
    lock_id = uuid.uuid4().hex
    unlock_at = datetime.utcnow() + timedelta(seconds=req.unlock_in)

    record = {
        "message": req.message,
        "unlock_at": unlock_at.isoformat(),
    }
    # записываем с небольшим запасом (ttl+60s)
    await store_set(lock_id, record, req.unlock_in)
    return {"id": lock_id}


@router.get("/timelock/open/{lock_id}")
async def open_timelock(lock_id: str):
    rec = await store_get(lock_id)
    if rec is None:
        # либо ещё не создали, либо истёк TTL
        raise HTTPException(status_code=404, detail="Not Found")

    unlock_at = datetime.fromisoformat(rec["unlock_at"])
    if datetime.utcnow() < unlock_at:
        # ещё рано
        raise HTTPException(status_code=403, detail="Too early")

    # возвращаем сообщение и удаляем запись
    await store_delete(lock_id)
    return {"message": rec["message"]}
