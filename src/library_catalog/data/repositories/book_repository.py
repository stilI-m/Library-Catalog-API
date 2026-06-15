from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.library_catalog.data.models.book import Book
from src.library_catalog.data.repositories.base_repository import BaseRepository


class BookRepository(BaseRepository[Book]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Book)
    async def find_by_filters(self, title: str = None, author: str = None, genre: str | None = None, year: int | None = None, available: bool | None = None, limit: int = 20, offset: int = 0) -> list[Book]:
        """search books by filters"""
        stmt = select(Book)
        if title:
            stmt = stmt.where(Book.title.ilike(f"%{title}%"))
        if author:
            stmt = stmt.where(Book.author.ilike(f"%{author}%"))
        if genre:
            stmt = stmt.where(Book.genre == genre)
        if year:
            stmt = stmt.where(Book.year == year)
        if available is not None:
            stmt = stmt.where(Book.available == available)
        stmt = stmt.limit(limit).offset(offset)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())
    async def find_by_isbn(self, isbn: str) -> Book | None:
        """search books by isbn"""
        pass
    async def count_by_filters(self, title: str = None, author: str = None, genre: str | None = None, year: int | None = None, available: bool | None = None, limit: int = 20, offset: int = 0) -> int:
        """search count of books by filters"""