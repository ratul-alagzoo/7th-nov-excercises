from fastapi import FastAPI, APIRouter

from api import index_controller

router = APIRouter()

@router.get("/")
def get_server_status():
    return  "Server is up and running"

def register_routers(app: FastAPI):
    app.include_router(router=router, tags=["Health Check"])
    app.include_router(router=index_controller.router, tags=["Hello"])