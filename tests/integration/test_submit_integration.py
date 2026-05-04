def test_submit(client):
    payload = {"user": "bob", "data": {"a": 1}}
    res = client.post("/api/submit", json=payload)
    assert res.status_code == 201
    assert res.json()["received"]["user"] == "bob"
