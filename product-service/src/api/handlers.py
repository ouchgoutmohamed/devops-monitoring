from flask import jsonify, request
from ..core.storage import product_storage

def get_products():
    products = product_storage.get_all_products()
    return jsonify(products), 200

def get_product(product_id):
    product = product_storage.get_product_by_id(product_id)
    if product is None:
        return jsonify({"error": "Product not found"}), 404
    return jsonify(product), 200

def add_product():
    data = request.get_json()
    new_product = product_storage.add_product(data)
    return jsonify(new_product), 201