import sqlalchemy
import sqlite3
from sqlalchemy import Table, MetaData, create_engine, Column, Integer, String, Boolean


engin = create_engine("sqlite:///example.db")
metadata = MetaData()

users_table = Table(
    "users",
    metadata,
    Column("Id", Integer, primary_key=True),
    Column("username", String(32), unique=True),
    Column("is_staff", Boolean, default=False),
)

if __name__ == "__main__":
    metadata.create_all(engin)