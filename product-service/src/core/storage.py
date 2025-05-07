class ProductStorage:
    def __init__(self):
        self._storage = {}  # In-memory storage

    def add_product(self, product_data):
        """Adds a new product to the storage."""
        product_id = f"prod_{len(self._storage) + 1}"
        # Assuming product_data is a dictionary.
        # We add an 'id' to it and store it.
        new_product = {**product_data, "id": product_id}
        self._storage[product_id] = new_product
        return new_product  # Return the created product dictionary

    def get_product_by_id(self, product_id):
        """Retrieves a product by its ID."""
        return self._storage.get(product_id)

    def get_all_products(self):
        """Retrieves all products from the storage."""
        return list(self._storage.values())

# Create a singleton instance of ProductStorage to be used by other modules
product_storage = ProductStorage()