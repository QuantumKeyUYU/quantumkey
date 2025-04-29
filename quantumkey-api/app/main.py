from fastapi import FastAPI

# импортируем все роутеры
from app.pq_signature     import router as pq_router
from app.threshold_vault  import router as threshold_router
from app.vdf              import router as vdf_router
from app.timelock         import router as timelock_router

app = FastAPI()

# монтируем их на свои префиксы
app.include_router(pq_router,        prefix="/pq")
app.include_router(threshold_router, prefix="/threshold")
app.include_router(vdf_router,       prefix="/vdf")
app.include_router(timelock_router,  prefix="/timelock")
