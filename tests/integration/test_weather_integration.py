def test_weather_default(client):
    res = client.get("/api/weather")
    assert res.status_code == 200
    assert res.json()["city"] == "Seattle"

def test_weather_custom(client):
    res = client.get("/api/weather?city=Paris")
    assert res.status_code == 200
    assert res.json()["city"] == "Paris"
