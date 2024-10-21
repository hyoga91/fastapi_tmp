from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine

users = Table("users", meta,
                Column("id", Integer, primary_key=True, autoincrement=True),
                Column("nombre", String(255), nullable=False),
                Column("email", String(255), nullable=False, unique=True),
                Column("password", String(255), nullable=False),
                Column("disabled", Boolean))

meta.create_all(engine)