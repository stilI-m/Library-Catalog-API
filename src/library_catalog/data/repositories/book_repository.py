from sqlalchemy import select, func
from sqlalchemy.ext.asyncio import AsyncSession

from src.library_catalog.data.models.book import Book
from src.library_catalog.data.repositories.base_repository import BaseRepository


class BookRepository(BaseRepository[Book]):
    def __init__(self, session: AsyncSession):
        super().__init__(session, Book)
    def _apply_filters(self, stmt, title, author, genre, year, available):
        """apply filters for assignment"""
        if title: stmt.where(Book.title.ilike(f'%{title}%'))
        if author: stmt.where(Book.author.ilike(f'%{author}%'))
        if genre: stmt.where(Book.genre == genre)
        if year: stmt.where(Book.year == year)
        if available is not None: stmt.where(Book.available == available)
        return stmt
    async def find_with_count(self, limit: int = 20, offset: int = 0, **kwargs) -> tuple[list[Book], int]:
        """It searches for books by filters and immediately returns their total number."""
        count_col = func.count().over().label('total_count')
        stmt = select(Book, count_col)
        stmt = self._apply_filters(stmt, **kwargs)
        stmt = stmt.limit(limit).offset(offset)
        result = await self.session.execute(stmt)
        rows = result.all()
        total = rows[0][1] if rows else 0
        books = [row[0] for row in rows]
        return books, total
    async def find_by_filters(self, limit: int = 20, offset: int = 0, **kwargs) -> list[Book]:
        """search books by filters"""
        stmt = self._apply_filters(select(Book), **kwargs)
        stmt = stmt.limit(limit).offset(offset)
        result = await self.session.execute(stmt)
        return list(result.scalars().all())
    async def find_by_isbn(self, isbn: str) -> Book | None:
        """search books by isbn"""
        stmt = select(Book).where(Book.isbn == isbn)
        result = await self.session.execute(stmt)
        # scalar_one_or_none() вернет либо книгу, либо None
        return result.scalar_one_or_none()
    async def count_by_filters(self, **kwargs) -> int:
        """search count of books by filters"""
        stmt = self._apply_filters(select(func.count()).select_from(Book), **kwargs)
        return (await self.session.execute(stmt)).scalar() or 0