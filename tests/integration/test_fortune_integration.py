def test_fortune(client):
    res = client.get("/api/fortune")
    assert res.status_code == 200
    assert "fortune" in res.json()
