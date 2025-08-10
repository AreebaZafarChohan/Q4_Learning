import os
from dotenv import load_dotenv
from agents import OpenAIChatCompletionsModel, RunConfig
from openai import AsyncOpenAI

# load env file
load_dotenv()

# get gemini api key
gemini_api_key = os.getenv("GEMINI_API_KEY")

# check api key exists or not
if not gemini_api_key:
    raise ValueError("Your GEMINI_API_KEY is not set. Please ensure that it is set into your .env file.")

# create external client and model

external_client =  AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client, # type: ignore
    tracing_disabled=True
)

