def test_add_favorite(client):
    res = client.post("/api/favorites", json={"id": 99})
    assert res.status_code == 201
    assert res.json()["current_favorites"] == [99]

def test_get_favorites(client):
    client.post("/api/favorites", json={"id": 1})
    client.post("/api/favorites", json={"id": 2})
    res = client.get("/api/favorites")
    assert res.status_code == 200
    assert res.json()["favorites"] == [1, 2]
