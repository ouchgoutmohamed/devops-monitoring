import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
    stages: [
        { duration: '30s', target: 100 }, // Ramp up to 100 users over 30 seconds
        { duration: '10m', target: 100 },  // Stay at 100 users for 10 minutes
        { duration: '30s', target: 0 },    // Ramp down to 0 users
    ],
};

export default function () {
    // Use service names as defined in your docker-compose.yml
    // and ensure the API paths are correct for each service.
    const productResponse = http.get('http://product-service:5001/api/products'); 
    const orderResponse = http.get('http://order-service:5002/api/orders'); // Assuming /api/orders, adjust if different     
    const inventoryResponse = http.get('http://inventory-service:5003/inventory/some_product_id'); // Adjust with a valid product ID or general inventory endpoint

    check(productResponse, {
        'product status is 200': (r) => r.status === 200,
    });
    check(orderResponse, {
        'order status is 200': (r) => r.status === 200, // Changed check name for clarity
    });
    check(inventoryResponse, {
        'inventory status is 200': (r) => r.status === 200,
    });

    sleep(1); // Wait for 1 second before the next iteration
}