FastAPI Demo - Products API
A simple FastAPI application demonstrating GET and POST endpoints for product management and inventory tracking.

Features
GET /: Welcome endpoint
GET /products/: Get all products
GET /products/{product_id}: Get a specific product by ID
POST /products/: Create a new product
Setup
Create and activate virtual environment:

python -m venv myenv
myenv\Scripts\activate.ps1  # Windows PowerShell
Install dependencies:

pip install fastapi uvicorn
Run the application:

uvicorn main:app --reload
Access the API:

API: http://localhost:8000
Interactive docs: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
Project Structure
invoTrack/
├── main.py          # FastAPI application with endpoints
├── models.py        # Pydantic models
├── .gitignore       # Git ignore file
└── README.md        # This file
API Usage Examples
Get all products
curl http://localhost:8000/products/
Get product by ID
curl http://localhost:8000/products/1
Create a new product
curl -X POST "http://localhost:8000/products/" \
     -H "Content-Type: application/json" \
     -d '{
       "id": 5,
       "name": "Monitor",
       "description": "4K monitor",
       "price": 299.99,
       "quantity": 15
     }'
Models
Product
id: integer
name: string
description: string
price: float
quantity: integer
Built With
FastAPI - Modern, fast web framework for building APIs
Pydantic - Data validation using Python type hints
Uvicorn - ASGI server implementation
