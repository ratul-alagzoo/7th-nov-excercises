
from interfaces.temp_conversion_response_type import TemperatureConversionResponse


def convert_temperature(from_temp: str,  to_temp: str, val: float) -> TemperatureConversionResponse:
    c = "C"
    k = "K"
    f = "F"
    if from_temp == to_temp:
        return  TemperatureConversionResponse(
            converted_val=0,
            hasError=True,
            message="Source and Destination type can not be same"
        )
    converted_val = None
    if from_temp == c and to_temp == f:
        converted_val = _celsius_to_fahrenheit(val)
    elif from_temp == f and to_temp == c:
        converted_val =  _fahrenheit_to_celsius(val)
    elif from_temp == f and to_temp == k:
        converted_val = _fahrenheit_to_kelvin(val)
    elif from_temp == k and to_temp == f:
        converted_val = _kelvin_to_fahrenheit(val)
    elif from_temp == c and to_temp == k:
        converted_val = _celsius_to_kelvin(val)
    elif from_temp == k and to_temp == c:
        converted_val = _kelvin_to_celsius(val)

    if converted_val is None:
        return TemperatureConversionResponse(
            hasError=True,
            converted_val=0,
            message="Invalid operation"
        )
    return  TemperatureConversionResponse(
        hasError=True,
        converted_val=converted_val,
        message=f"{val}\u00B0{from_temp} -- > {converted_val}\u00B0{to_temp}"
    )

def _celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def _fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def _celsius_to_kelvin(c):
    return c + 273.15

def _kelvin_to_celsius(k):
    return k - 273.15

def _fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def _kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32