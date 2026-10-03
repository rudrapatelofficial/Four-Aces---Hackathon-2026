from google import genai
from dotenv import load_dotenv
from fastapi import FastAPI
import os

from google.genai.types import EditImageConfig
app = FastAPI()

@app.get("/make_prediction")
async def make_prediction(heartbeat: str, glucose: str, Interbeat_interval: str, EDA: str)->str:
    load_dotenv()
    google_api_key = os.getenv("GEMINI_API_KEY")
    client = genai.Client(api_key=google_api_key)

    input_text = f"What is the likelihood of this person having prediabetes? Output your answer as a number from 0.01 to 1, with 0.01 being a 1% chance and 1 being 100%. Information to use: HeartBeat: {heartbeat}, glucose: {glucose}, Interbeat_interval: {Interbeat_interval}, EDA: {EDA}"
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=input_text
    )
    return str(interaction.output_text)




