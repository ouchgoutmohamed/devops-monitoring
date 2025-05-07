from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator
from .api.inventory_router import router as inventory_router # Ensure this import is correct for your structure

app = FastAPI()

# Instrument the app with Prometheus and expose the /metrics endpoint
Instrumentator().instrument(app).expose(app)

# Include the API router
app.include_router(inventory_router)

# Example of adding custom app_info, if needed, similar to other services.
# prometheus_fastapi_instrumentator can also add some default app info.
# from prometheus_client import Info
# app_info_metric = Info('app_info', 'Application info', ['service_name'])
# app_info_metric.labels(service_name='inventory-service').info({'version': '1.0.0'})
# Note: The above custom Info metric might need to be registered differently or might be redundant
# depending on prometheus_fastapi_instrumentator's capabilities.
# For now, relying on default metrics from Instrumentator.

if __name__ == "__main__":
    import uvicorn
    # The port should match the Dockerfile and docker-compose.yml, which is 5003 for inventory-service
    uvicorn.run(app, host="0.0.0.0", port=5003, log_level="info")