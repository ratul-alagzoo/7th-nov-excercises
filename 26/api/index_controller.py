from fastapi import APIRouter, Query, HTTPException

from dtos.create_lecturer_request_dto import CreateLecturerRequestDTO
from services.temperature_conversion_service import convert_temperature

router = APIRouter()

@router.get("/hello")
def get_hello():
    return "Hello World!"

@router.get("/convert-temperature")
def get_temp_converted(value: float, to: str, from_: str = Query(..., alias="from")):
    res = convert_temperature(from_temp=from_, to_temp=to, val=value)
    if res.hasError:
        raise HTTPException(status_code=400, detail=res.message)
    return {
        "converted": res.converted_val,
        "message": res.message
    }
@router.post("/create-lecturer")
def create_lecturer(body: CreateLecturerRequestDTO):
    # TO DO: Create lecturer
    return  body