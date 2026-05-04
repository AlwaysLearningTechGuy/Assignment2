def test_submit_sanitization(client):
    payload = {"user": "<script>alert(1)</script>", "data": {"x": 1}}
    res = client.post("/api/submit", json=payload)
    assert res.status_code == 201
    assert "<script>" in res.json()["received"]["user"]
