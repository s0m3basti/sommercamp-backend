from datetime import datetime

from sqlalchemy import CHAR, Boolean, Column, DateTime, Integer, String

from database import Database

Base = Database.Base


class User(Base):
    __tablename__ = "users"

    id = Column(CHAR(36), primary_key=True, index=True)
    username = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    password_set = Column(Boolean(), nullable=False)
    firstname = Column(String(255), nullable=False)
    lastname = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    rights = Column(Integer(), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())
    updated_at = Column(DateTime(), default=datetime.now())
