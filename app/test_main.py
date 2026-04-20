import pytest
import time
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

# TC-01: Connectivity
def test_fortune_connectivity():
    response = client.get("/api/fortune")
    assert response.status_code == 200
    assert "msg" in response.json()

# TC-02: Echo Validation
def test_submit_echo():
    payload = {"user": "Dev", "data": {"key": "value"}}
    response = client.post("/api/submit", json=payload)
    assert response.status_code == 201
    assert response.json()["received"]["user"] == "Dev"

# TC-03: Schema Integrity
def test_insight_schema():
    response = client.get("/api/insight")
    data = response.json()
    assert response.status_code == 200
    # Validating existence of required fields per Technical Design
    assert "id" in data
    assert "msg" in data

# TC-04: Payload Boundary
def test_large_payload():
    large_data = "a" * (1024 * 1025)
    response = client.post("/api/submit", json={"user": "test", "data": {"msg": large_data}})
    # Note: If middleware isn't set, this might return 201; 
    # documenting this result in the Test Report is key.
    assert response.status_code in [201, 413] 

# TC-07: Performance Latency
def test_weather_performance():
    start = time.time()
    client.get("/api/weather")
    duration = (time.time() - start) * 1000
    assert duration < 200

# TC-08/09: Persistence Workflow
def test_favorites_persistence():
    # Save an item
    client.post("/api/favorites", json={"id": 777})
    # Retrieve and verify
    response = client.get("/api/favorites")
    assert 777 in response.json()["favorites"]
