# quantumkey-api/app/pq_signature.py

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# -- модели запросов/ответов --------------------------------------

class SignRequest(BaseModel):
    message: str

class SignResponse(BaseModel):
    signature: str
    phase_proof: str

class VerifyRequest(BaseModel):
    message: str
    signature: str
    phase_proof: str

class VerifyResponse(BaseModel):
    valid: bool

# -- конечные точки ------------------------------------------------

@router.post("/sign", response_model=SignResponse)
async def sign(req: SignRequest):
    """
    Пока просто возвращаем фиктивную подпись и доказательство.
    """
    sig = f"falcon_sig_{req.message}"
    proof = f"proof_of_{req.message}"
    return SignResponse(signature=sig, phase_proof=proof)


@router.post("/verify", response_model=VerifyResponse)
async def verify(req: VerifyRequest):
    """
    Всегда возвращаем, что подпись корректна, если она
    совпадает с тем, что выдали при /sign.
    """
    expected_sig   = f"falcon_sig_{req.message}"
    expected_proof = f"proof_of_{req.message}"

    valid = (req.signature == expected_sig and req.phase_proof == expected_proof)
    return VerifyResponse(valid=valid)
