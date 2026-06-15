from typing import Generic, TypeVar, Type
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, session: AsyncSession, model: Type[T]):
        self.session = session
        self.model = model
    async def create(self, **kwargs) -> T:
        """Create a new instance of the model"""
        instance = self.model(**kwargs)
        self.session.add(instance)
        await self.session.commit()
        await self.session.refresh(instance)
        return instance
    async def get_by_id(self, id: UUID) -> T | None:
        """Retrieve a model by its id"""
        return await self.session.get(self.model, id)
    async def update(self, id: UUID, **kwargs) -> T | None:
        """Update an existing instance of the model"""
        pass
    async def delete(self, id: UUID) -> bool:
        """Delete an existing instance of the model"""
        el = await self.session.get(self.model, id)
        if el is None:
            return False
        else:
            await self.session.delete(el)
            await self.session.commit()
            return True
    async def get_all(self, limit: int = 100, offset: int = 0,) -> list[T]:
        """Retrieve all instances of the model"""
        stmt = select(self.model).limit(limit).offset(offset)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())

