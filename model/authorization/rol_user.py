from sqlalchemy import Table, Column, DateTime, func
from sqlalchemy.sql.sqltypes import Integer, String, Boolean
from config.db import meta, engine

roles = Table("rol_user", meta,
                Column("rol_id", Integer, ForeignKey("roles.id"), primary_key=True,nullable=False),
                Column("user_id", Integer, ForeignKey("users.id"), primary_key=True,nullable=False),
                Column("created_at", DateTime(timezone=True), server_default=func.now()),
                Column("updated_at", DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
                )
meta.create_all(engine)