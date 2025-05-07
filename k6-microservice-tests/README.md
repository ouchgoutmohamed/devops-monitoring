### Step 1: Install k6

If you haven't installed k6 yet, you can do so by following the instructions on the [k6 installation page](https://k6.io/docs/getting-started/installation/).

### Step 2: Create a Load Testing Script

Create a new directory for your load testing project, and inside that directory, create a file named `load-test.js`. This script will simulate user traffic to your services.

```javascript
// filepath: c:\Users\AdMin\Desktop\prometheus\projet devops\load-test\load-test.js

import http from 'k6/http';
import { check, sleep } from 'k6';

export let options = {
    stages: [
        { duration: '30s', target: 100 }, // Ramp up to 100 users over 30 seconds
        { duration: '1m', target: 100 },  // Stay at 100 users for 1 minute
        { duration: '30s', target: 0 },    // Ramp down to 0 users
    ],
};

export default function () {
    const productResponse = http.get('http://localhost:5001/products'); // Adjust the endpoint as necessary
    const orderResponse = http.get('http://localhost:5002/orders');     // Adjust the endpoint as necessary
    const inventoryResponse = http.get('http://localhost:5003/inventory'); // Adjust the endpoint as necessary

    check(productResponse, {
        'product status is 200': (r) => r.status === 200,
    });
    check(orderResponse, {
        'order status is 200': (r) => r.status === 200,
    });
    check(inventoryResponse, {
        'inventory status is 200': (r) => r.status === 200,
    });

    sleep(1); // Wait for 1 second before the next iteration
}
```

### Step 3: Create a Dockerfile for k6

Create a `Dockerfile` in the same directory to build a Docker image for running k6.

```dockerfile
# filepath: c:\Users\AdMin\Desktop\prometheus\projet devops\load-test\Dockerfile

FROM loadimpact/k6:latest

COPY load-test.js /load-test.js

ENTRYPOINT ["k6", "run", "/load-test.js"]
```

### Step 4: Update `docker-compose.yml`

Add a new service for k6 in your existing `docker-compose.yml` file. This will allow you to run the load test as part of your Docker setup.

```yaml
# Add this section to your existing docker-compose.yml

  load-test:
    build:
      context: ./load-test
    depends_on:
      - product-service
      - order-service
      - inventory-service
    networks:
      - app-network
```

### Step 5: Build and Run the Load Test

1. Navigate to the directory containing your `docker-compose.yml` file.
2. Build the Docker images and start the services:

   ```bash
   docker-compose up --build
   ```

3. Once the services are up and running, you can run the load test by executing:

   ```bash
   docker-compose run load-test
   ```

### Step 6: Monitor with Prometheus

Ensure that your Prometheus instance is configured to scrape metrics from your services. You should see increased CPU usage in Prometheus as k6 generates load on your services.

### Conclusion

You now have a load testing setup using k6 that simulates user traffic to your product, order, and inventory services. You can adjust the load test parameters in the `load-test.js` file to simulate different traffic patterns as needed.