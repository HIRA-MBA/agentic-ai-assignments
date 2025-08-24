from pydantic import BaseModel


class WeatherOutput(BaseModel):
    city: str
    region: str
    country: str
    temperature_c: float
    temperature_f: float
    condition: str
    humidity: int
    wind_kph: float


