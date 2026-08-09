from fastapi import FastAPI
from model import product
from database import session, engine
import database_model

app=FastAPI()

database_model.Base.metadata.create_all(bind=engine)
@app.get("/")

def greet():
    return "hi How are you?"

products = [
    product(id=1, name="phone", description="nice features", price=10000.00, quantity=24),
    product(id=2, name="laptop", description="powerful performance", price=50000.99, quantity=10),
    product(id=3, name="tablet", description="portable and versatile", price=30000.50, quantity=15),
    product(id=4, name="smartwatch", description="fitness tracking", price=20000.00, quantity=20)
]

def init_db():
    db = session()
    for product in products:
        db.add(database_model.product(product.model_dump() ))

@app.get("/products")
def get_all_products():
    db = session() 
    return products

@app.get("/product/{id}")
def get_product_id(id: int):
    for product in products:
        if product.id == id:
            return product

    return "product not found"


@app.post("/product")
def add_product(product: product):
    products.append(product)
    return product

@app.put("/product")
def update_product(id: int, updated_product: product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = updated_product
            return "updated successfully"

    return "product not found"

@app.delete("/product")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted successfully"

    return "product not found"