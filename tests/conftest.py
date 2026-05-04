import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.test_utils import reset_state

@pytest.fixture(autouse=True)
def reset_everything():
    reset_state()

@pytest.fixture
def client():
    return TestClient(app)
