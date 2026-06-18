from typing import Generic, TypeVar, Type
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import AsyncSession

from src.library_catalog.core.exceptions import AppException

T = TypeVar('T')

class BaseRepository(Generic[T]):
    def __init__(self, session: AsyncSession, model: Type[T]):
        self.session = session
        self.model = model
    async def create(self, **kwargs) -> T:
        """Create a new instance of the model"""
        instance = self.model(**kwargs)
        try:
            self.session.add(instance)
            await self.session.commit()
            await self.session.refresh(instance)
            return instance
        except IntegrityError:
            await self.session.rollback()
            raise AppException(message="Книга с таким ISBN уже существует в каталоге", status_code=409)
    async def get_by_id(self, id: UUID) -> T | None:
        """Retrieve a model by its id"""
        return await self.session.get(self.model, id)
    async def update(self, id: UUID, **kwargs) -> T | None:
        """Update an existing instance of the model"""
        # 1. Если нам не передали полей для обновления, просто возвращаем книгу
        if not kwargs:
            return await self.get_by_id(id)

        # 2. Достаем объект из базы (используем уже написанный тобой метод)
        instance = await self.get_by_id(id)
        if not instance:
            return None

        # 3. Меняем только те поля, которые пришли в kwargs (например, available=False)
        for key, value in kwargs.items():
            setattr(instance, key, value)

        # 4. Сохраняем изменения в базу
        try:
            await self.session.commit()
            await self.session.refresh(instance)
            return instance
        except Exception:
            # На случай непредвиденных ошибок БД отменяем транзакцию
            await self.session.rollback()
            raise
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

