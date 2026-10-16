"""Conexão e definição da tabela 'usuarios'."""
from datetime import datetime

from sqlalchemy import (Column, Date, DateTime, Integer, MetaData, String,
                        Table, create_engine)

from config import DB_URL

engine = create_engine(DB_URL, echo=False)
metadata = MetaData()

usuarios = Table(
    "usuarios", metadata,
    Column("id", Integer, primary_key=True),
    Column("nome", String(50), nullable=False, index=True),
    Column("cpf", String(14), nullable=False),
    Column("email", String(100), nullable=False, unique=True),
    Column("telefone", String(20), nullable=False),
    Column("data_nascimento", Date, nullable=False),
    Column("created_on", DateTime(), default=datetime.now),
    Column("updated_on", DateTime(), default=datetime.now,
           onupdate=datetime.now),
)
