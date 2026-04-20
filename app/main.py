from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
import time
import random

app = FastAPI(title="Wonderful and Mysterious API")

# Simulated In-Memory Database
db = {"favorites": []}

# Models
class FavoriteItem(BaseModel):
    id: int

class SubmitPayload(BaseModel):
    user: str
    data: dict

# --- Wonderful Endpoints ---

@app.get("/api/weather")
async def get_weather(city: str = "Seattle"):
    # Mock data logic
    return {"city": city, "temp": "22°C", "condition": "Partly Cloudy"}

@app.get("/api/timezone")
async def get_timezone(offset: int = 0):
    # Simulated UTC to Local logic
    current_utc = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    return {"timezone": f"GMT{offset:+}", "local_time": current_utc, "offset": offset}

@app.get("/api/insight")
async def get_insight(topic: str = "general"):
    # TC-03 Refinement: No 'ts' field included
    return {"id": random.randint(100, 999), "msg": f"Strategic insight regarding {topic}."}

# --- Mysterious Endpoints ---

@app.get("/api/fortune")
async def get_fortune():
    fortunes = ["A grand adventure awaits.", "Data is the new oil.", "Check your logs frequently."]
    return {"id": random.randint(1, 100), "msg": random.choice(fortunes)}

@app.post("/api/submit", status_code=201)
async def post_submit(payload: SubmitPayload):
    # TC-02: Echoing back the received data
    return {"status": "Created", "received": payload}

@app.post("/api/favorites", status_code=201)
async def add_favorite(item: FavoriteItem):
    db["favorites"].append(item.id)
    return {"message": "Saved", "current_favorites": db["favorites"]}

@app.get("/api/favorites")
async def get_favorites():
    return {"favorites": db["favorites"]}
