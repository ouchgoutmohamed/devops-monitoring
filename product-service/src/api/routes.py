# File: product-service/src/api/routes.py
from flask import Blueprint

from .handlers import get_products, get_product, add_product

api_bp = Blueprint('api', __name__)

api_bp.route('/products', methods=['GET'])(get_products)
api_bp.route('/products/<productId>', methods=['GET'])(get_product)
api_bp.route('/products', methods=['POST'])(add_product)

def setup_routes(app):
    app.register_blueprint(api_bp, url_prefix='/api')