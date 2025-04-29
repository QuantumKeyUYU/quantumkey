from fastapi import FastAPI
from app.vdf       import router as vdf_router
from app.timelock  import router as timelock_router
from app.threshold_vault import router as threshold_router
from app.pq_signature   import router as pq_router

app = FastAPI()

app.include_router(vdf_router,        prefix="/vdf")
app.include_router(timelock_router,   prefix="/timelock")
app.include_router(threshold_router,  prefix="/threshold")
app.include_router(pq_router,         prefix="/pq")
