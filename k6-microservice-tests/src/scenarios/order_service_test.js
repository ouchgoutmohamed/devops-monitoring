// filepath: c:\Users\AdMin\Desktop\prometheus\projet devops\load-test\load-test.js

import http from 'k6/http';
import { sleep, check } from 'k6';

export let options = {
    vus: 100, // Number of virtual users
    duration: '30s', // Duration of the test
};

export default function () {
    // Simulate requests to the product service
    let productResponse = http.get('http://localhost:5001/products');
    check(productResponse, { 'status was 200': (r) => r.status === 200 });

    // Simulate requests to the order service
    let orderResponse = http.get('http://localhost:5002/orders');
    check(orderResponse, { 'status was 200': (r) => r.status === 200 });

    // Simulate requests to the inventory service
    let inventoryResponse = http.get('http://localhost:5003/inventory');
    check(inventoryResponse, { 'status was 200': (r) => r.status === 200 });

    sleep(1); // Sleep for 1 second between iterations
}