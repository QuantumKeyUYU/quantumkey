from fastapi import APIRouter
from fastapi.params import Body
from pydantic import BaseModel

router = APIRouter()

class PQRequest(BaseModel):
    message: str

class PQResponse(BaseModel):
    signature: str
    phase_proof: str

@router.post("/sign", response_model=PQResponse)
async def sign_and_verify(req: PQRequest = Body(...)):
    # простая заглушка
    return {
        "signature":      "falcon_sig_stub",
        "phase_proof":    "falcon_sig_stub"
    }
