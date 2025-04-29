from fastapi import APIRouter, HTTPException
from fastapi.params import Body
from pydantic import BaseModel

router = APIRouter()

class TimelockRequest(BaseModel):
    message: str
    unlock_in: int

class TimelockResponse(BaseModel):
    id: str

@router.post("/create", response_model=TimelockResponse)
async def create_timelock(req: TimelockRequest = Body(...)):
    # заглушка: сразу запрещено
    raise HTTPException(status_code=403)

@router.get("/open/{lock_id}")
async def open_timelock(lock_id: str):
    # заглушка: сразу запрещено
    raise HTTPException(status_code=403)
