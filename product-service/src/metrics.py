from prometheus_client import Counter, Histogram, Gauge

# Define counters for total requests and status codes
app_requests_total = Counter('app_requests_total', 'Total number of requests', ['method', 'endpoint', 'service'])
http_requests_by_status_code_total = Counter('http_requests_by_status_code_total', 'Total number of HTTP requests by status code', ['code', 'service'])

# Define histograms for request latency
app_request_latency_seconds_bucket = Histogram('app_request_latency_seconds_bucket', 'Request latency in seconds', ['method', 'endpoint', 'service'])

# Define a counter for products viewed
products_viewed_total = Counter('products_viewed_total', 'Total number of products viewed', ['product_id', 'service'])

# Define a gauge for the product catalog size
product_catalog_size = Gauge('product_catalog_size', 'Total number of products available', ['service'])