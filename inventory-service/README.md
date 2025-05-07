# Python Inventory Service

This project is a Python-based Inventory Service designed to manage and provide information about product stock levels. It exposes a RESTful API for interacting with inventory data.

## Features

- Retrieve current stock levels for specific products.
- Decrease stock levels when orders are confirmed.
- Increase stock levels when new shipments arrive.
- Prometheus metrics for monitoring API requests and stock levels.

## API Endpoints

### GET /inventory/{productId}

Retrieves the current stock level for a specific product.

**Response:**
```json
{
  "product_id": "prod_123",
  "stock_level": 75,
  "last_updated": "2025-05-06T12:00:00Z"
}
```

**Error Response (404 Not Found):**
```json
{
  "error": "Product inventory not found"
}
```

### POST /inventory/decrease

Decreases the stock level for a product.

**Request Body:**
```json
{
  "product_id": "prod_123",
  "quantity_decreased": 2
}
```

**Response:**
```json
{
  "product_id": "prod_123",
  "new_stock_level": 73,
  "status": "Stock updated"
}
```

**Error Responses:**
- 400 Bad Request: 
```json
{
  "error": "Insufficient stock for product prod_123"
}
```
- 409 Conflict: 
```json
{
  "error": "Product not found"
}
```

### POST /inventory/increase

Increases the stock level for a product.

**Request Body:**
```json
{
  "product_id": "prod_123",
  "quantity_increased": 50
}
```

**Response:**
```json
{
  "product_id": "prod_123",
  "new_stock_level": 123,
  "status": "Stock updated"
}
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-inventory-service
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python -m src.inventory_app.main
   ```

## Testing

To run the tests, use:
```
pytest tests/
```

## Metrics

The service includes Prometheus metrics for monitoring:

- Total API requests
- Request latency
- Current stock levels
- Stock updates
- Inventory API errors

## License

This project is licensed under the MIT License.