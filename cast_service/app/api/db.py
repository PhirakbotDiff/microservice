import os

from sqlalchemy import (Column, Integer, MetaData, String, Table,
                        create_engine, ARRAY)

from databases import Database
from .config import settings

print("cast service",settings.DATABASE_URI)
DATABASE_URI = settings.DATABASE_URI

engine = create_engine(DATABASE_URI)
metadata = MetaData()

casts = Table(
    'casts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('nationality', String(20)),
)

database = Database(DATABASE_URI)