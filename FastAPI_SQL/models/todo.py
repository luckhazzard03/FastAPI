from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import declarative_base

from db import session

Base = declarative_base()

class Todo(Base):
    '''uyhiuhuio'''
    def __init__(self, __tablename__ = "todos"):
        self.id = Column(Integer, primary_key=True)
        self.text = Column(String)
        self.is_done = Column(Boolean, default=False)

Base.metadata.create_all(session)
