from agents import function_tool

@function_tool(name_override="get_weather",description_override="describe the weather of city")
async def weather_tool(city:str):
    "return the weather of the city"
    print("weather tool fire -->")

    return f"weather of {city} is 30 degree celsius"