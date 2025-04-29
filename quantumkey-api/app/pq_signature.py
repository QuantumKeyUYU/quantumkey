from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(prefix="/pq", tags=["pq-signature"])

class SignReq(BaseModel):
    message: str

class SignResp(BaseModel):
    signature: str
    phase_proof: str

class VerifyReq(BaseModel):
    signature: str
    phase_proof: str
    message: str

@router.post("/sign", response_model=SignResp)
async def sign(req: SignReq):
    sig   = f"falcon_sig_{req.message}"
    proof = f"phase_proof_{req.message}"
    return {"signature": sig, "phase_proof": proof}

@router.post("/verify")
async def verify(req: VerifyReq):
    valid = req.signature.startswith("falcon_sig_") and req.phase_proof.startswith("phase_proof_")
    return {"valid": valid}
