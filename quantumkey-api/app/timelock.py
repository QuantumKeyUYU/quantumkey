from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
import uuid

router = APIRouter(prefix="/timelock")

class CreateRequest(BaseModel):
    message: str
    unlock_in: int  # секунд

class CreateResponse(BaseModel):
    id: str
    unlock_at: datetime

class OpenResponse(BaseModel):
    message: str

# простейшее in-memory хранилище
_store: dict[str, dict] = {}

@router.post("/create", response_model=CreateResponse)
async def create(req: CreateRequest):
    id_ = str(uuid.uuid4())
    unlock_at = datetime.utcnow() + timedelta(seconds=req.unlock_in)
    # на старте без шифра
    _store[id_] = {"msg": req.message, "unlock_at": unlock_at}
    return CreateResponse(id=id_, unlock_at=unlock_at)

@router.get("/open/{id}", response_model=OpenResponse)
async def open_lock(id: str):
    info = _store.get(id)
    if not info:
        raise HTTPException(404, "Not found")
    now = datetime.utcnow()
    if now < info["unlock_at"]:
        raise HTTPException(403, f"Еще рано, откроется в {info['unlock_at']}")
    return OpenResponse(message=info["msg"])
