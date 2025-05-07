
from datetime import datetime
from typing import Optional, Dict # Add Dict and Optional

# A simple in-memory storage for inventory
_inventory_db = {
    "product123": {"stock_level": 100, "last_updated": datetime.utcnow().isoformat()},
    "product456": {"stock_level": 50, "last_updated": datetime.utcnow().isoformat()},
}

class InventoryService:
    # def get_stock_level(self, product_id: str) -> dict | None: # ...existing code...
    def get_stock_level(self, product_id: str) -> Optional[Dict]: # Changed for Python 3.9 compatibility
        if product_id in _inventory_db:
            return {
                "product_id": product_id,
                "stock_level": _inventory_db[product_id]["stock_level"],
                "last_updated": _inventory_db[product_id]["last_updated"],
            }
        return None

    # def decrease_stock(self, product_id: str, quantity_decreased: int) -> int | None: # ...existing code...
    def decrease_stock(self, product_id: str, quantity_decreased: int) -> Optional[int]: # Changed for Python 3.9 compatibility
        item = self.get_stock_level(product_id)
        # Ensure item is not None and item is a dictionary before accessing "stock_level"
        if item and isinstance(item, dict) and item.get("stock_level", 0) >= quantity_decreased:
            _inventory_db[product_id]["stock_level"] -= quantity_decreased
            _inventory_db[product_id]["last_updated"] = datetime.utcnow().isoformat()
            return _inventory_db[product_id]["stock_level"]
        return None 

    def increase_stock(self, product_id: str, quantity_increased: int) -> int:
        if product_id not in _inventory_db:
            _inventory_db[product_id] = {"stock_level": 0, "last_updated": datetime.utcnow().isoformat()}
        
        _inventory_db[product_id]["stock_level"] += quantity_increased
        _inventory_db[product_id]["last_updated"] = datetime.utcnow().isoformat()
        return _inventory_db[product_id]["stock_level"]