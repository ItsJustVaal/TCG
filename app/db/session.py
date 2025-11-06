from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from app.core.settings import get_settings

settings = get_settings()

engine = create_async_engine(settings.DATABASE_URL, future=True, echo=False, pool_pre_ping=True)
AsyncSessionLocal: async_sessionmaker[AsyncSession] = async_sessionmaker(
    bind=engine, autoflush=False, expire_on_commit=False
)
