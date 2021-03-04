from fastapi import FastAPI

from .db.base import create_tables
from .v1 import router as v1_router


create_tables()
app = FastAPI()
app.include_router(v1_router, prefix="/api")
