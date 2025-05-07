from fastapi.testclient import TestClient
from inventory_app.main import app

client = TestClient(app)

def test_get_inventory_existing_product():
    response = client.get("/inventory/prod_123")
    assert response.status_code == 200
    assert response.json() == {
        "product_id": "prod_123",
        "stock_level": 75,
        "last_updated": "2025-05-06T12:00:00Z"
    }

def test_get_inventory_non_existing_product():
    response = client.get("/inventory/non_existing_product")
    assert response.status_code == 404
    assert response.json() == {"error": "Product inventory not found"}

def test_decrease_stock_success():
    response = client.post("/inventory/decrease", json={"product_id": "prod_123", "quantity_decreased": 2})
    assert response.status_code == 200
    assert response.json() == {
        "product_id": "prod_123",
        "new_stock_level": 73,
        "status": "Stock updated"
    }

def test_decrease_stock_insufficient():
    response = client.post("/inventory/decrease", json={"product_id": "prod_123", "quantity_decreased": 100})
    assert response.status_code == 400
    assert response.json() == {"error": "Insufficient stock for product prod_123"}

def test_increase_stock_success():
    response = client.post("/inventory/increase", json={"product_id": "prod_123", "quantity_increased": 50})
    assert response.status_code == 200
    assert response.json() == {
        "product_id": "prod_123",
        "new_stock_level": 123,
        "status": "Stock updated"
    }