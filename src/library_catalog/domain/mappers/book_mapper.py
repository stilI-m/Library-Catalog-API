from ...data.models.book import Book
from ...api.v1.schemas.book import ShowBook

class BookMapper:
    """Mapper for update Book entity in DTO"""
    @staticmethod
    def to_show_book(book: Book) -> ShowBook:
        return ShowBook.model_validate(book)
    @staticmethod
    def to_show_books(books: list[Book]) -> list[ShowBook]:
        """Update list of books"""
        return [ShowBook.model_validate(b) for b in books]