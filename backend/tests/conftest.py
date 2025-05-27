import pytest


@pytest.fixture
def fake_order_response():
    return {'order': [{'idOrder': 123, 'status': 'received'}]}