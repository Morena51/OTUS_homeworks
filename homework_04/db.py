import os

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://postgres:password@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=True)
async_session = AsyncSession(engine, expire_on_commit=False)
