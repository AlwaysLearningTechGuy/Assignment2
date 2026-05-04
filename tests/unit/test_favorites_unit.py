import pytest
from app.main import add_favorite, get_favorites, FavoriteItem, db

@pytest.mark.asyncio
async def test_add_favorite():
    await add_favorite(FavoriteItem(id=42))
    assert db["favorites"] == [42]

@pytest.mark.asyncio
async def test_get_favorites():
    db["favorites"] = [1, 2, 3]
    result = await get_favorites()
    assert result["favorites"] == [1, 2, 3]
