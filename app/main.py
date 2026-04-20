from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import random

app = FastAPI(title="Wonderful and Mysterious API")

# Simulated In-Memory Database for stateful testing
db = {"favorites": []}

class FavoriteItem(BaseModel):
    id: int

class SubmitPayload(BaseModel):
    user: str
    data: dict

@app.get("/api/weather")
async def get_weather(city: str = "Seattle"):
    return {"city": city, "temp": "22°C", "condition": "Partly Cloudy"}

@app.get("/api/insight")
async def get_insight(topic: str = "general"):
    # Clean version: simple id and msg
    return {"id": random.randint(100, 999), "msg": f"Strategic insight regarding {topic}."}

@app.get("/api/fortune")
async def get_fortune():
    fortunes = ["A grand adventure awaits.", "Data is the new oil.", "Expect the unexpected."]
    return {"id": random.randint(1, 100), "msg": random.choice(fortunes)}

@app.post("/api/submit", status_code=201)
async def post_submit(payload: SubmitPayload):
    return {"status": "Created", "received": payload}

@app.post("/api/favorites", status_code=201)
async def add_favorite(item: FavoriteItem):
    db["favorites"].append(item.id)
    return {"message": "Saved", "current_favorites": db["favorites"]}

@app.get("/api/favorites")
async def get_favorites():
    return {"favorites": db["favorites"]}
