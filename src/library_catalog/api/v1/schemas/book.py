from datetime import datetime
from uuid import UUID
from pydantic import BaseModel

class BookBase(BaseModel):
    """Базовая схема книги"""
    title: str
    author: str
    year: int
    genre: str
    pages: int

class BookCreate(BookBase):
    """Схема для того, что пользователь присылает при создании"""
    isbn: str | None = None
    description: str | None = None

class BookUpdate(BaseModel):
    """Схема для обновления (все поля необязательные)"""
    title: str | None = None
    author: str | None = None
    year: int | None = None
    genre: str | None = None
    pages: int | None = None
    available: bool | None = None

class ShowBook(BookBase):
    """Схема того, что мы отдаем пользователю в ответ (DTO)"""
    book_id: UUID
    available: bool
    isbn: str | None
    description: str | None
    extra: dict | None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True # Позволяет Pydantic читать данные напрямую из моделей SQLAlchemy