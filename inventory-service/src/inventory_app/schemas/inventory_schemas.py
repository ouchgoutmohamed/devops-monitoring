from pydantic import BaseModel
from typing import Optional

class InventoryResponseSchema(BaseModel):
    product_id: str
    stock_level: int
    last_updated: str

class DecreaseStockRequestSchema(BaseModel):
    product_id: str
    quantity_decreased: int

class IncreaseStockRequestSchema(BaseModel):
    product_id: str
    quantity_increased: int

class ErrorResponseSchema(BaseModel):
    error: str