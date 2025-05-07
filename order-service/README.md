# Order Service Project

## Overview
The Order Service is a microservice designed to handle the creation and management of customer orders. It provides a set of API endpoints for interacting with orders, allowing clients to create new orders and retrieve existing ones.

## Project Structure
```
order-service
├── src
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── models
│   │   ├── __init__.py
│   │   └── order.py
│   ├── routes
│   │   ├── __init__.py
│   │   └── order_routes.py
│   └── services
│       ├── __init__.py
│       └── order_service.py
├── tests
│   ├── __init__.py
│   ├── conftest.py
│   └── test_order_routes.py
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd order-service
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## API Endpoints

### Create Order
- **Endpoint:** `POST /orders`
- **Description:** Creates a new order.
- **Request Body:**
  ```json
  {
    "customer_id": "string",
    "items": [
      {
        "item_id": "string",
        "quantity": "integer"
      }
    ]
  }
  ```
- **Response:**
  - **201 Created:** Returns the created order details.
  - **400 Bad Request:** If the request body is invalid.

### Get Order
- **Endpoint:** `GET /orders/{orderId}`
- **Description:** Retrieves the details of a specific order by its ID.
- **Response:**
  - **200 OK:** Returns the order details.
  - **404 Not Found:** If the order does not exist.

## Usage Examples
- To create an order, send a POST request to `/orders` with the appropriate JSON body.
- To retrieve an order, send a GET request to `/orders/{orderId}`.

## Running the Application
To run the application, execute the following command:
```
uvicorn src.app:app --reload
```

## Testing
To run the tests, use the following command:
```
pytest
```

## License
This project is licensed under the MIT License.