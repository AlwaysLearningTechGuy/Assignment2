import pytest
from app.main import get_insight

@pytest.mark.asyncio
async def test_insight_default_topic():
    result = await get_insight()
    assert "Strategic insight" in result["msg"]

@pytest.mark.asyncio
async def test_insight_custom_topic():
    result = await get_insight(topic="AI")
    assert "AI" in result["msg"]
