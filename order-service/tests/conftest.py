import pytest

@pytest.fixture
def client():
    from src.app import app
    with app.test_client() as client:
        yield client