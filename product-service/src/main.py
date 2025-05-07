from flask import Flask
from .api.routes import setup_routes # Changed to relative import
from prometheus_flask_exporter import PrometheusMetrics
from flask import Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

def create_app():
    flask_app = Flask(__name__)
    
    metrics = PrometheusMetrics(flask_app, path='/metrics')
    
    setup_routes(flask_app)
    
    metrics.info('app_info', 'Application info', version='1.0.0')
    
    # The following manual metrics endpoint is redundant if PrometheusMetrics is used
    # and can be removed.
    # @flask_app.route('/metrics')
    # def metrics_endpoint():
    #     return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
      
    return flask_app

app = create_app() # Create app instance at module level for Gunicorn

if __name__ == "__main__":
    # This app.run is for direct execution, not for Gunicorn
    app.run(host='0.0.0.0', port=5001, debug=True)