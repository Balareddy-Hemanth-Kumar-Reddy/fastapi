from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

db_url = "postgresql://postgres:postgres@localhost:5433/fastapi"
engine = create_engine(db_url)
session = sessionmaker(autocommit=False, autoflush=True, bind=engine)