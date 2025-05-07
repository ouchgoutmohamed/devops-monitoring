import pytest
from src.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_create_order(client):
    response = client.post('/orders', json={
        'customer_id': '123',
        'items': [{'product_id': 'abc', 'quantity': 2}],
        'total_amount': 50.0
    })
    assert response.status_code == 201
    json_data = response.get_json()
    assert 'order_id' in json_data
    assert json_data['customer_id'] == '123' # Optional: assert more details

def test_get_order(client):
    # First, create an order to ensure it exists
    create_response = client.post('/orders', json={
        'customer_id': 'test_customer_get',
        'items': [{'product_id': 'prod_get', 'quantity': 1}],
        'total_amount': 25.0
    })
    assert create_response.status_code == 201
    created_order_data = create_response.get_json()
    order_id_to_get = created_order_data['order_id']

    # Now, try to get the created order
    response = client.get(f'/orders/{order_id_to_get}')
    assert response.status_code == 200
    retrieved_order_data = response.get_json()
    assert 'order_id' in retrieved_order_data
    assert retrieved_order_data['order_id'] == order_id_to_get
    assert retrieved_order_data['customer_id'] == 'test_customer_get'