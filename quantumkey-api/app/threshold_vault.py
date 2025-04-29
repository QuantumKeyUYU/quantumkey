from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class ThresholdRequest(BaseModel):
    message: str
    n: int
    k: int

@router.post("/split")
async def threshold_split(req: ThresholdRequest):
    return {
        "shares": ["stub_share1", "stub_share2"]
    }

class CombineRequest(BaseModel):
    shares: list

@router.post("/combine")
async def threshold_combine(req: CombineRequest):
    return {
        "combined_message": "stub_combined_message"
    }
