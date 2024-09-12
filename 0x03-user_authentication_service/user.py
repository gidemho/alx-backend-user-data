#!/usr/bin/env python3
"""
User model definition using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

# Initialize the declarative base for SQLAlchemy
Base = declarative_base()


class User(Base):

    """
    SQLAlchemy User model for the users table.
    Attributes:
        - id: integer, primary key
        - email: string, non-nullable
        - hashed_password: string, non-nullable
        - session_id: string, nullable
        - reset_token: string, nullable
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)


# Create a SQLite in-memory database (for testing purposes)
if __name__ == "__main__":
    engine = create_engine('sqlite:///:memory:')
    Base.metadata.create_all(engine)