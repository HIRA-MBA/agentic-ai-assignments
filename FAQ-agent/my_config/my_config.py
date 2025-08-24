from decouple import config
from openai import AsyncOpenAI
from agents import OpenAIChatCompletionsModel


gemini_api_key=config("GEMINI_API_KEY")
gemini_base_url=config("GEMINI_BASE_URL")
gemini_model_name=config("GEMINI_MODEL_NAME")

client=AsyncOpenAI(api_key=gemini_api_key,base_url=gemini_base_url)

Model=OpenAIChatCompletionsModel(model=gemini_model_name,openai_client=client)