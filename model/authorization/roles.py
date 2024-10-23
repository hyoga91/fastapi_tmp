from sqlalchemy import Table, Column, DateTime, func
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine

roles = Table("roles", meta,
                Column("id", Integer, primary_key=True, autoincrement=True),
                Column("nombre", String(255), nullable=False),
                Column("email", String(255), nullable=False, unique=True),
                Column("password", String(255), nullable=False),
                Column("disabled", Boolean),
                Column("created_at", DateTime(timezone=True), server_default=func.now()),
                Column("updated_at", DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
                )

meta.create_all(engine)