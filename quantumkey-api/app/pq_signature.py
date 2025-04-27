# quantumkey-api/app/pq_signature.py

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class SignRequest(BaseModel):
    message: str

class SignResponse(BaseModel):
    falcon_signature: str
    phase_proof: str

@router.post("/sign", response_model=SignResponse, tags=["PQ-Signature"])
async def sign_message(req: SignRequest):
    # — TODO: заменить на реальную Falcon-подпись
    falcon_sig = f"falcon_sig_of_{req.message}"
    # — TODO: real phase proof (VDF+mix)
    phase_proof = f"phase_proof_of_{req.message}"
    return SignResponse(falcon_signature=falcon_sig, phase_proof=phase_proof)

class VerifyRequest(BaseModel):
    message: str
    falcon_signature: str
    phase_proof: str

class VerifyResponse(BaseModel):
    valid: bool

@router.post("/verify", response_model=VerifyResponse, tags=["PQ-Signature"])
async def verify_message(req: VerifyRequest):
    # — TODO: заменить на реальную проверку Falcon и фазу
    valid = (
        req.falcon_signature == f"falcon_sig_of_{req.message}" and
        req.phase_proof      == f"phase_proof_of_{req.message}"
    )
    return VerifyResponse(valid=valid)
