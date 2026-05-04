from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_weather_default_city():
    response = client.get("/api/weather")
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "Seattle"
    assert "temp" in data
    assert "condition" in data

def test_weather_custom_city():
    response = client.get("/api/weather?city=Portland")
    assert response.status_code == 200
    data = response.json()
    assert data["city"] == "Portland"

def test_insight_default_topic():
    response = client.get("/api/insight")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "msg" in data
    assert "general" in data["msg"]

def test_insight_custom_topic():
    response = client.get("/api/insight?topic=technology")
    assert response.status_code == 200
    data = response.json()
    assert "technology" in data["msg"]

def test_fortune():
    response = client.get("/api/fortune")
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert "msg" in data

def test_submit_payload():
    payload = {
        "user": "alice",
        "data": {"value": 42}
    }
    response = client.post("/api/submit", json=payload)
    assert response.status_code == 201
    data = response.json()
    assert data["status"] == "Created"
    assert data["received"]["user"] == "alice"
    assert data["received"]["data"]["value"] == 42

def test_add_favorite():
    response = client.post("/api/favorites", json={"id": 7})
    assert response.status_code == 201
    data = response.json()
    assert data["message"] == "Saved"
    assert 7 in data["current_favorites"]

def test_get_favorites():
    # Add a known favorite first
    client.post("/api/favorites", json={"id": 99})

    response = client.get("/api/favorites")
    assert response.status_code == 200
    data = response.json()
    assert "favorites" in data
    assert 99 in data["favorites"]
