from fastapi import APIRouter
from pydantic import BaseModel
from typing import Any, Dict

router = APIRouter()

class SignReq(BaseModel):
    message: str

class SignRes(BaseModel):
    falcon_sig: str
    phase_proof: str

@router.post("/sign", response_model=SignRes)
async def sign(req: SignReq) -> SignRes:
    # простая «заглушка» с константными строками
    return SignRes(
        falcon_sig="falcon_sig_stub",
        phase_proof="phase_proof_stub",
    )

class VerifyReq(BaseModel):
    message: str
    signature: Dict[str, Any]

class VerifyRes(BaseModel):
    valid: bool

@router.post("/verify", response_model=VerifyRes)
async def verify(req: VerifyReq) -> VerifyRes:
    # всегда «валидно»
    return VerifyRes(valid=True)
