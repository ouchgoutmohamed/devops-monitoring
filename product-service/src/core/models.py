class Product:
    def __init__(self, id, name, description, price, category, stock_available=True):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.stock_available = stock_available

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "stock_available": self.stock_available
        }