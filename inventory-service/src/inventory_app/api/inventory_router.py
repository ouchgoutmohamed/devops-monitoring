from fastapi import APIRouter, HTTPException
# from inventory_app.models.inventory_item import InventoryItem # Adjusted to absolute import
from pydantic import BaseModel
# from inventory_app.services.inventory_service import InventoryService # ...existing code...
from ..services.inventory_service import InventoryService # Changed to relative import

router = APIRouter()
inventory_service = InventoryService()

class DecreaseStockRequest(BaseModel):
    product_id: str
    quantity_decreased: int

class IncreaseStockRequest(BaseModel):
    product_id: str
    quantity_increased: int

class StockResponse(BaseModel):
    product_id: str
    new_stock_level: int
# ...existing code...
    status: str

class InventoryResponse(BaseModel):
    product_id: str
    stock_level: int
    last_updated: str

@router.get("/inventory/{product_id}", response_model=InventoryResponse)
async def get_inventory(product_id: str):
    stock_info = inventory_service.get_stock_level(product_id)
    if stock_info is None:
        raise HTTPException(status_code=404, detail="Product inventory not found")
    return stock_info

@router.post("/inventory/decrease", response_model=StockResponse)
async def decrease_stock(request: DecreaseStockRequest):
    new_stock_level = inventory_service.decrease_stock(request.product_id, request.quantity_decreased)
    if new_stock_level is None:
        raise HTTPException(status_code=400, detail=f"Insufficient stock for product {request.product_id}")
    return StockResponse(product_id=request.product_id, new_stock_level=new_stock_level, status="Stock updated")

@router.post("/inventory/increase", response_model=StockResponse)
async def increase_stock(request: IncreaseStockRequest):
    new_stock_level = inventory_service.increase_stock(request.product_id, request.quantity_increased)
    return StockResponse(product_id=request.product_id, new_stock_level=new_stock_level, status="Stock updated")