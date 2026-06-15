import uuid
from datetime import datetime

from sqlalchemy import Boolean, DateTime, Integer, String, Text, JSON
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func
from ...core.database import Base

class Book(Base):
    """info about a book"""
    __tablename__ = 'books'
    book_id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True,)
    title: Mapped[str] = mapped_column(String(500), index=True, nullable=False,)
    author: Mapped[str] = mapped_column(String(300), index=True, nullable=False,)
    year: Mapped[int] = mapped_column(Integer, index=True, nullable=False,)
    genre: Mapped[str] = mapped_column(String(100), index=True, nullable=False,)
    pages: Mapped[int] = mapped_column(Integer)
    available: Mapped[bool] = mapped_column(Boolean, default=True, index=True)
    isbn: Mapped[str | None] = mapped_column(String(20), unique=True, )
    description: Mapped[str | None] = mapped_column(Text, )
    extra: Mapped[dict | None] = mapped_column(JSON, )
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), index=True, nullable=False,)
    updated_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), onupdate= func.now(), index=True, nullable=False,)
    def __repr__(self):
        return f"<Book(id={self.book_id}, title='{self.title}')>"