from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from config.db import engine

Base = declarative_base()

class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False, unique=True)
    password = Column(String(255), nullable=False)

Base.metadata.create_all(engine)