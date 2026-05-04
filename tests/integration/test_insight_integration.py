def test_insight_default(client):
    res = client.get("/api/insight")
    assert res.status_code == 200
    assert "Strategic insight" in res.json()["msg"]

def test_insight_custom(client):
    res = client.get("/api/insight?topic=finance")
    assert res.status_code == 200
    assert "finance" in res.json()["msg"]
