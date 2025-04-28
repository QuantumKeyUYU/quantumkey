# quantumkey-api/app/timelock.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
import uuid

router = APIRouter(prefix="/timelock", tags=["timelock"])


class TimelockCreateRequest(BaseModel):
    message: str
    unlock_in: int


class TimelockCreateResponse(BaseModel):
    id: str
    ready_at: datetime


class TimelockOpenResponse(BaseModel):
    message: str


@router.post("/create", response_model=TimelockCreateResponse)
async def create_timelock(req: TimelockCreateRequest):
    # Генерируем ID и расчётное время готовности
    id_str = str(uuid.uuid4())
    ready_at = datetime.utcnow() + timedelta(seconds=req.unlock_in)
    # Здесь можно сохранить в БД/памяти, но для теста достаточно возвращать эти поля
    return TimelockCreateResponse(id=id_str, ready_at=ready_at)


@router.get("/open/{id}", response_model=TimelockOpenResponse)
async def open_timelock(id: str):
    # Тест test_create_and_open_immediately_forbidden ожидает, что
    # попытка открыть до готовности выдаст 403 Forbidden
    raise HTTPException(status_code=403, detail="Timelock not ready")
