import pytest
from app.main import (
    get_weather,
    get_insight,
    get_fortune,
    post_submit,
    add_favorite,
    get_favorites,
    SubmitPayload,
    FavoriteItem,
)

@pytest.mark.asyncio
async def test_get_weather_default():
    result = await get_weather()
    assert result["city"] == "Seattle"
    assert "temp" in result
    assert "condition" in result

@pytest.mark.asyncio
async def test_get_weather_custom():
    result = await get_weather(city="Portland")
    assert result["city"] == "Portland"

@pytest.mark.asyncio
async def test_get_insight_default():
    result = await get_insight()
    assert "general" in result["msg"]
    assert isinstance(result["id"], int)

@pytest.mark.asyncio
async def test_get_insight_custom():
    result = await get_insight(topic="ai")
    assert "ai" in result["msg"]

@pytest.mark.asyncio
async def test_get_fortune():
    result = await get_fortune()
    assert "id" in result
    assert "msg" in result

@pytest.mark.asyncio
async def test_post_submit():
    payload = SubmitPayload(user="bob", data={"x": 1})
    result = await post_submit(payload)
    assert result["status"] == "Created"
    assert result["received"].user == "bob"

@pytest.mark.asyncio
async def test_add_favorite():
    item = FavoriteItem(id=123)
    result = await add_favorite(item)
    assert "Saved" in result["message"]
    assert 123 in result["current_favorites"]

@pytest.mark.asyncio
async def test_get_favorites():
    result = await get_favorites()
    assert "favorites" in result
    assert isinstance(result["favorites"], list)
