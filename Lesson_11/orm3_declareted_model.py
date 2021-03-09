import sqlalchemy
import sqlite3
from sqlalchemy import Table, MetaData, create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapper
from datetime import datetime

engin = create_engine("sqlite:///example2.db")
Base = declarative_base(bind=engin)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(32), unique=True)
    is_staff = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow())


if __name__ == "__main__":
    Base.metadata.create_all(engin)