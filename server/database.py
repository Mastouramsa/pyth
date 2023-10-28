#database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///../chinook.db", echo=True)

session = Session(bind=engine)
