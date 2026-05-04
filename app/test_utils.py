from app.rate_limiter import rate_limiter
from app.main import db

def reset_state():
    db["favorites"].clear()
    rate_limiter.reset()
