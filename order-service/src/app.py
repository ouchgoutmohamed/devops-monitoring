
from flask import Flask
from .routes.order_routes import order_bp
from asgiref.wsgi import WsgiToAsgi
from prometheus_flask_exporter import PrometheusMetrics # Add this import

def _create_flask_app():
    flask_app_instance = Flask(__name__)
    
    # Initialize Prometheus metrics on the Flask app instance
    # This will make /metrics available on the Flask app
    PrometheusMetrics(flask_app_instance) # Add this line
    
    flask_app_instance.register_blueprint(order_bp)
    return flask_app_instance

# Create the raw Flask app instance first
_flask_app = _create_flask_app()

# This is the app Uvicorn will serve (ASGI-wrapped)
app = WsgiToAsgi(_flask_app)

if __name__ == "__main__":
    # This block is for running directly with `python src/app.py`
    # It uses Flask's built-in development server with the raw Flask app.
    _flask_app.run(host='0.0.0.0', port=5002, debug=True)