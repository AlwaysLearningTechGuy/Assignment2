import pytest
import time
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

# TC-01: Connectivity
def test_fortune_connectivity():
    response = client.get("/api/fortune")
    assert response.status_code == 200
    assert response.json()["msg"] != ""

# TC-02: Echo Validation
def test_submit_echo():
    payload = {"user": "Dev", "data": {"key": "value"}}
    response = client.post("/api/submit", json=payload)
    assert response.status_code == 201
    assert response.json()["received"]["user"] == "Dev"

# TC-03: Schema Integrity (Validated without 'ts')
def test_insight_schema():
    response = client.get("/api/insight")
    data = response.json()
    assert "id" in data
    assert "msg" in data
    assert "ts" not in data  # Ensuring refinement is followed

# TC-07: Performance Latency
def test_weather_performance():
    start = time.time()
    client.get("/api/weather")
    duration = (time.time() - start) * 1000
    assert duration < 200

# TC-08/09: Persistence Workflow
def test_favorites_persistence():
    # Clear favorites for isolation
    from .main import db
    db["favorites"] = []
    
    # Save
    client.post("/api/favorites", json={"id": 777})
    # Retrieve
    response = client.get("/api/favorites")
    assert 777 in response.json()["favorites"]
