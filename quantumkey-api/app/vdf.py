from fastapi import APIRouter
import time

router = APIRouter()

@router.get("/eval")
async def eval_vdf(input_data: str, delay: int = 5):
    # здесь будет реальная VDF-имплементация, пока просто sleep
    time.sleep(delay)
    proof = f"proof_of_{input_data}"
    return {"result": proof}
