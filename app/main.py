from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import random

from app.rate_limiter import rate_limiter

app = FastAPI(title="Wonderful and Mysterious API v2.0")

# In-memory database
db = {"favorites": []}


class FavoriteItem(BaseModel):
    id: int


class SubmitPayload(BaseModel):
    user: str
    data: dict


# ---------------------------
# Rate Limiting Middleware
# ---------------------------
@app.middleware("http")
async def rate_limit_middleware(request: Request, call_next):
    client_ip = request.client.host

    # Return JSONResponse instead of raising HTTPException
    if not rate_limiter.is_allowed(client_ip):
        return JSONResponse(
            status_code=429,
            content={"detail": "Too Many Requests"},
        )

    return await call_next(request)


# ---------------------------
# API Endpoints
# ---------------------------

@app.get("/api/weather")
async def get_weather(city: str = "Seattle"):
    return {"city": city, "temp": "22°C", "condition": "Partly Cloudy"}


@app.get("/api/insight")
async def get_insight(topic: str = "general"):
    return {
        "id": random.randint(100, 999),
        "msg": f"Strategic insight regarding {topic}.",
    }


@app.get("/api/fortune")
async def get_fortune():
    fortunes = [
        "A grand adventure awaits.",
        "Data is the new oil.",
        "Expect the unexpected.",
    ]
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
