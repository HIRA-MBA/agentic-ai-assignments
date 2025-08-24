from agents import function_tool
import requests
from my_config.my_config import weather_api_key
from dataclass.dataclass import WeatherOutput


@function_tool
def get_weather(city: str) -> WeatherOutput:
    """
    Fetch current weather data for a given city using WeatherAPI.

    Args:
        city (str): The EXACT city name provided by the user. 
        Do not modify, correct, or replace this value.
    
    """
    url = f"http://api.weatherapi.com/v1/current.json?key={weather_api_key}&q={city}&aqi=no"
    print(f"DEBUG >> Fetching weather for: {city}")  # 👈 add logging
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch weather data: {response.status_code}")

    data = response.json()
    if "error" in data:
        raise Exception(data["error"].get("message", "Unknown error."))

    current = data["current"]
    location = data["location"]

    return WeatherOutput(
        city=location["name"],
        region=location["region"],
        country=location["country"],
        temperature_c=current["temp_c"],
        temperature_f=current["temp_f"],
        condition=current["condition"]["text"],
        humidity=current["humidity"],
        wind_kph=current["wind_kph"],
    )
