from fastapi import Depends, FastAPI
from model import product
from database import session, engine
import database_model
from sqlalchemy.orm import Session 

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

def db_get():
    try:
        db = session()
    finally:
        db.close()
    
def init_db():
    db = session()
    count=db.query(database_model.product).count()
    if count == 0:
        for product in products:
            db.add(database_model.product(**product.model_dump()))

        db.commit()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(db_get)):
    db_products=db.query(database_model.product).all()

    
    return db_products

@app.get("/product/{id}")
def get_product_id(id: int, db: Session = Depends(db_get)):
    db_product=db.query(database_model.product).filter(database_model.product.id == id).first()
    if db_product:
        return db_product

    return "product not found"


@app.post("/product")
def add_product(product: product, db: Session = Depends(db_get)):
    db.add(database_model.product(**product.model_dump()))
    db.commit()
    return product

@app.put("/product")
def update_product(id: int, updated_product: product, db: Session = Depends(db_get)):
    db_product=db.query(database_model.product).filter(database_model.product.id == id).first()
    if db_product:
        db_product.name = updated_product.name
        db_product.description = updated_product.description
        db_product.price = updated_product.price
        db_product.quantity = updated_product.quantity
        db.commit()
        return "updated successfully"
    else:
        return "product not found"

@app.delete("/product")
def delete_product(id: int, db: Session = Depends(db_get)):
    db_product=db.query(database_model.product).filter(database_model.product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "product deleted successfully"
    else:
        return "product not found"