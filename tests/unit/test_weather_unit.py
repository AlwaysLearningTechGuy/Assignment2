import pytest
from app.main import get_weather

@pytest.mark.asyncio
async def test_weather_default_city():
    result = await get_weather()
    assert result["city"] == "Seattle"

@pytest.mark.asyncio
async def test_weather_custom_city():
    result = await get_weather(city="Tokyo")
    assert result["city"] == "Tokyo"
