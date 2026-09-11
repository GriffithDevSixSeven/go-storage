from config import db_settings

from sqlalchemy.ext.asyncio import create_async_engine,async_sessionmaker,AsyncSession
from fastapi import Depends
from typing import Annotated,AsyncGenerator

engine = create_async_engine(db_settings.DB_URL)

session_factory = async_sessionmaker(engine)

async def get_session() -> AsyncGenerator[AsyncSession,None]:
    async with session_factory() as session:
        yield session


SessionDep = Annotated[AsyncSession,Depends(get_session)]
