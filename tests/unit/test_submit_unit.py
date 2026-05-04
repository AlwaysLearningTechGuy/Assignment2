import pytest
from app.main import post_submit, SubmitPayload

@pytest.mark.asyncio
async def test_submit_payload():
    payload = SubmitPayload(user="alice", data={"x": 1})
    result = await post_submit(payload)
    assert result["status"] == "Created"
    assert result["received"].user == "alice"
