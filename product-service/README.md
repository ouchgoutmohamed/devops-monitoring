# Product Service

This project is a simple product management service that provides an API for managing and retrieving product information. It includes endpoints for listing products, retrieving product details, and adding new products to the catalog.

## Project Structure

```
product-service
├── src
│   ├── __init__.py
│   ├── main.py
│   ├── api
│   │   ├── __init__.py
│   │   ├── handlers.py
│   │   └── routes.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── storage.py
│   └── metrics.py
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd product-service
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python src/main.py
   ```

## API Usage

### Retrieve All Products
- **Endpoint:** `GET /products`
- **Description:** Retrieves a list of all available products.

### Retrieve Product Details
- **Endpoint:** `GET /products/{productId}`
- **Description:** Retrieves details for a specific product by its ID.

### Add a New Product
- **Endpoint:** `POST /products`
- **Description:** Adds a new product to the catalog.

## Metrics

The service exposes Prometheus metrics to monitor the performance and usage of the API. Metrics include request counts, latency, and product catalog size.

## License

This project is licensed under the MIT License.