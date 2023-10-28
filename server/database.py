#database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

engine = create_engine("sqlite:///../chinook.db", echo=True)
## Creates a session to interact with the database.
session = Session(bind=engine)
