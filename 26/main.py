import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

from api.index import register_routers

logger = logging.getLogger("uvicorn")

@asynccontextmanager
async  def lifespan(app: FastAPI):
    logger.info("Server started")
    yield
    logger.info("Server stopped")

app = FastAPI(
    title="Course work for 7th Nov.",
    description="API DOCS",
    lifespan=lifespan
)

register_routers(app)
