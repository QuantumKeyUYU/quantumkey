from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/threshold", tags=["threshold"])

class SplitRequest(BaseModel):
    message: str
    n: int
    k: int

class CombineRequest(BaseModel):
    shares: list[str]

@router.post("/split")
async def split(req: SplitRequest):
    # VERY BASIC stub: n частей текста
    shares = [f"share_{i+1}_of_{req.message}" for i in range(req.n)]
    return {"shares": shares}

@router.post("/combine")
async def combine(req: CombineRequest):
    if not req.shares:
        return {"message": ""}
    # откусываем суффикс
    parts = req.shares[0].split("_of_", 1)
    return {"message": parts[1] if len(parts) > 1 else ""}
