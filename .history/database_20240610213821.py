from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_URL = "sqlite+aiosqlite://fastapi-app.db"
engine = create_async_engine(DB_URL, echo=True)
