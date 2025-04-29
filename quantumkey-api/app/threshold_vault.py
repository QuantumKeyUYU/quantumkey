from fastapi import APIRouter
from fastapi.params import Body
from pydantic import BaseModel

router = APIRouter()

class ThresholdRequest(BaseModel):
    shares: int

class ThresholdResponse(BaseModel):
    status: str

@router.post("/split", response_model=ThresholdResponse)
async def split_secret(req: ThresholdRequest = Body(...)):
    return {"status": "ok"}

@router.post("/combine", response_model=ThresholdResponse)
async def combine_secret(req: ThresholdRequest = Body(...)):
    return {"status": "ok"}
