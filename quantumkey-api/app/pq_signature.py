from fastapi import APIRouter
from pydantic import BaseModel
import hashlib

router = APIRouter(prefix="/pq", tags=["pq-signature"])

# Pydantic-схемы
class SignRequest(BaseModel):
    message: str

class SignResponse(BaseModel):
    signature: str

class VerifyRequest(BaseModel):
    message: str
    signature: str

class VerifyResponse(BaseModel):
    valid: bool

# Заглушки для Falcon и VDF — потом заменим на реальные имплементации
def falcon_sign(message: str) -> str:
    # TODO: заменить на настоящую Falcon-подпись
    return "falcon_sig_stub"

def falcon_verify(message: str, sig: str) -> bool:
    # TODO: заменить на настоящую проверку Falcon-подписи
    return sig == "falcon_sig_stub"

def vdf_eval(message: str) -> str:
    # TODO: заменить на VDF Eval
    return hashlib.sha256(message.encode()).hexdigest()

# Гибридная логика
def hybrid_sign(message: str) -> str:
    falcon_sig = falcon_sign(message)
    vdf_digest = vdf_eval(message)
    return f"{falcon_sig}:{vdf_digest}"

def hybrid_verify(message: str, signature: str) -> bool:
    try:
        falcon_sig, vdf_digest = signature.split(":", 1)
    except ValueError:
        return False
    return falcon_verify(message, falcon_sig) and (vdf_eval(message) == vdf_digest)

# Эндпоинты
@router.post("/sign", response_model=SignResponse)
async def sign(req: SignRequest):
    sig = hybrid_sign(req.message)
    return SignResponse(signature=sig)

@router.post("/verify", response_model=VerifyResponse)
async def verify(req: VerifyRequest):
    valid = hybrid_verify(req.message, req.signature)
    return VerifyResponse(valid=valid)
