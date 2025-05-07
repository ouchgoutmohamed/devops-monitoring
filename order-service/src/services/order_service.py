from datetime import datetime
from typing import List, Dict, Optional

class Order:
    def __init__(self, order_id: str, customer_id: str, items: List[Dict], status: str, total_amount: float):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.status = status
        self.total_amount = total_amount
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def update_order(self, items: Optional[List[Dict]] = None, status: Optional[str] = None):
        if items is not None:
            self.items = items
        if status is not None:
            self.status = status
        self.updated_at = datetime.utcnow()

class OrderService:
    def __init__(self):
        self.orders = {}

    def create_order(self, order_id: str, customer_id: str, items: List[Dict], total_amount: float) -> Order:
        order = Order(order_id, customer_id, items, status="created", total_amount=total_amount)
        self.orders[order_id] = order
        return order

    def get_order(self, order_id: str) -> Optional[Order]:
        return self.orders.get(order_id)

    def update_order(self, order_id: str, items: Optional[List[Dict]] = None, status: Optional[str] = None) -> Optional[Order]:
        order = self.get_order(order_id)
        if order:
            order.update_order(items, status)
        return order

    def list_orders(self) -> List[Order]:
        return list(self.orders.values())
order_service = OrderService()