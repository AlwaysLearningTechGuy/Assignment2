import pytest
from app.main import get_fortune

@pytest.mark.asyncio
async def test_fortune_structure():
    result = await get_fortune()
    assert "msg" in result
    assert "id" in result
