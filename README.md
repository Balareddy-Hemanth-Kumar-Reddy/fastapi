FastAPI Products API

A small FastAPI project for managing a products/inventory list, backed by PostgreSQL through SQLAlchemy. It started as a way to practice building a REST API with a real database instead of an in-memory list, so it's kept intentionally simple.

What it does

Basic CRUD on a single product resource: id, name, description, price, and quantity. On startup, the app seeds the database with a handful of sample products (phone, laptop, tablet, smartwatch) if the table is empty, so you have data to play with right away.

Endpoints
Method	Route	Description
GET	/	Health check / greeting
GET	/products	Get all products
GET	/product/{id}	Get a single product by ID
POST	/product	Add a new product
PUT	/product?id={id}	Update an existing product
DELETE	/product?id={id}	Delete a product
Tech stack
FastAPI — the web framework
SQLAlchemy — ORM / database layer
PostgreSQL — database
Pydantic — request validation
Setup
Clone the repo and create a virtual environment:
bash
   python -m venv myenv
   myenv\Scripts\activate.ps1   # Windows PowerShell
   # source myenv/bin/activate  # macOS/Linux
Install dependencies:
bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary
Make sure PostgreSQL is running and update the connection string in database.py to match your setup:
python
   db_url = "postgresql://postgres:postgres@localhost:5433/fastapi"

By default it points at a local Postgres instance on port 5433 with a database called fastapi — adjust the username, password, port, and database name for your environment.

Run the app:
bash
   uvicorn main:app --reload
Open it up:
API: http://localhost:8000
Swagger docs: http://localhost:8000/docs
ReDoc: http://localhost:8000/redoc
Project structure
.
├── main.py             # FastAPI app and route handlers
├── model.py             # Pydantic schema for request/response validation
├── database.py           # DB engine and session setup
├── database_model.py      # SQLAlchemy table definition
└── README.md
Example requests

Get all products:

bash
curl http://localhost:8000/products

Get a single product:

bash
curl http://localhost:8000/product/1

Add a product:

bash
curl -X POST http://localhost:8000/product \
  -H "Content-Type: application/json" \
  -d '{"id": 5, "name": "Monitor", "description": "4K monitor", "price": 299.99, "quantity": 15}'

Update a product:

bash
curl -X PUT "http://localhost:8000/product?id=1" \
  -H "Content-Type: application/json" \
  -d '{"id": 1, "name": "Phone", "description": "updated features", "price": 12000.00, "quantity": 30}'

Delete a product:

bash
curl -X DELETE "http://localhost:8000/product?id=1"
Notes
This is a learning/practice project, so there's no auth on the endpoints yet — anyone hitting the API can create, edit, or delete products.
The database URL is currently hardcoded in database.py; moving it to an environment variable would be a good next step before deploying anywhere.
