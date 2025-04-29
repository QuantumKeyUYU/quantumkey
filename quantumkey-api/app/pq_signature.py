from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SignRequest(BaseModel):
    message: str

class SignResponse(BaseModel):
    signature: str
    phase_proof: str

@router.post("/sign", response_model=SignResponse)
async def sign(req: SignRequest):
    # пока просто возвращаем «заглушки»
    sig = f"falcon_sig_stub:{req.message}"
    proof = f"phase_proof_stub:{req.message}"
    return {"signature": sig, "phase_proof": proof}

class VerifyRequest(BaseModel):
    message: str
    signature: str

class VerifyResponse(BaseModel):
    valid: bool

@router.post("/verify", response_model=VerifyResponse)
async def verify(req: VerifyRequest):
    # всегда валидно
    return {"valid": True}
