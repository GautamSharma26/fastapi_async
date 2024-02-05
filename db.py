from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from config import DevelopmentConfig

SQLALCHEMY_DATABASE_URL = DevelopmentConfig.SQLALCHEMY_DATABASE_URL
engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = async_sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


async def get_db():
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        await db_session.close()
