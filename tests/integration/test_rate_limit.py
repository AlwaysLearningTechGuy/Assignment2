def test_rate_limit_enforced(client):
    # First 10 requests allowed
    for _ in range(10):
        res = client.get("/api/weather")
        assert res.status_code == 200

    # 11th request blocked
    res = client.get("/api/weather")
    assert res.status_code == 429
