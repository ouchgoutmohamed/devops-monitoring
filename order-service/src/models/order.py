class Order:
    def __init__(self, order_id, customer_id, items, status, total_amount, created_at, updated_at):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.status = status
        self.total_amount = total_amount
        self.created_at = created_at
        self.updated_at = updated_at

    def update_order(self, items=None, status=None, total_amount=None):
        if items is not None:
            self.items = items
        if status is not None:
            self.status = status
        if total_amount is not None:
            self.total_amount = total_amount
        self.updated_at = datetime.utcnow()  # Assuming datetime is imported

    @classmethod
    def create_order(cls, customer_id, items, total_amount):
        order_id = generate_order_id()  # Assuming a function to generate unique order IDs
        created_at = datetime.utcnow()  # Assuming datetime is imported
        return cls(order_id, customer_id, items, 'pending', total_amount, created_at, created_at)