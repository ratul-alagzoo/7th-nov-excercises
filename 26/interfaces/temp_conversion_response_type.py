from pydantic.v1 import BaseModel


class TemperatureConversionResponse(BaseModel):
    hasError: bool
    message: str
    converted_val: float
