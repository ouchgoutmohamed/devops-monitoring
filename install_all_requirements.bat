@echo off
echo Installing requirements for Product Service...
cd my-product-service
pip install -r src\requirements.txt
cd ..

echo Installing requirements for Order Service...
cd order-service
pip install -r requirements.txt
cd ..

echo Installing requirements for Inventory Service...
cd inventory-service
pip install -r requirements.txt
cd ..

echo All requirements installed.
pause