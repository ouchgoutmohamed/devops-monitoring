# Load Testing with k6

This project sets up a load testing environment using k6 to simulate user traffic to your services. Below are the steps and details for creating and running the load tests.

## Project Structure

```
my-k6-load-testing-project
├── load-test
│   ├── load-test.js
│   └── Dockerfile
├── docker-compose.yml
└── README.md
```

## Step 1: Install k6

If you haven't installed k6 yet, you can do so by following the instructions on the [k6 installation page](https://k6.io/docs/getting-started/installation/).

## Step 2: Create a Load Testing Script

The load testing script is located in `load-test/load-test.js`. This script simulates user traffic to your services by performing HTTP GET requests to specified endpoints.

## Step 3: Create a Dockerfile for k6

The `Dockerfile` in the `load-test` directory is used to build a Docker image for running k6. It specifies the base image and copies the load test script into the image.

## Step 4: Update `docker-compose.yml`

The `docker-compose.yml` file defines the services for the Docker application, including the load-test service. It specifies the build context, dependencies on other services, and the network configuration.

## Step 5: Build and Run the Load Test

1. Navigate to the directory containing your `docker-compose.yml` file.
2. Build the Docker images and start the services:

   ```bash
   docker-compose up --build
   ```

3. Once the services are up and running, you can run the load test by executing:

   ```bash
   docker-compose run load-test
   ```

## Step 6: Monitor with Prometheus

Ensure that your Prometheus instance is configured to scrape metrics from your services. You should see increased CPU usage in Prometheus as k6 generates load on your services.

## Conclusion

You now have a load testing setup using k6 that simulates user traffic to your product, order, and inventory services. You can adjust the load test parameters in the `load-test/load-test.js` file to simulate different traffic patterns as needed.