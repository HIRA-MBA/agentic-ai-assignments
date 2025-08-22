
from agents import RunContextWrapper,Agent
from pydantic import BaseModel

class UserName(BaseModel):
    name: str   
    query: str


async def dynamic_instructions(
    context: RunContextWrapper[UserName],
    agent: Agent[UserName]
) -> str:
    query = context.context.query.strip().lower()  
    user_name = context.context.name

    if "sannata hotel" in query:
        return (
            f"You are the booking officer for Sannata Hotel. "
            f"The user's name is {user_name}. "
            f"Charges: 5000 PKR per night. "
            f"Available rooms: 10 deluxe, 5 standard."
        )
    elif "samama hotel" in query:
        return (
            f"You are the booking officer for Samama Hotel. "
            f"The user's name is {user_name}. "
            f"Charges: 3500 PKR per night. "
            f"Available rooms: 8 deluxe, 12 standard."
        )
    else:
        return f"The user's name is {user_name}. Help them with general questions."