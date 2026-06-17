from uuid import UUID

from ..core.exceptions import AppException, NotFoundException

class BookNotFoundException(NotFoundException):
    """book not found"""
    def __init__(self, book_id: UUID):
        super().__init__(resource="Book", identifier=book_id)

class BookAlreadyExistsException(AppException):
    """book already exists"""
    def __init__(self, isbn: str):
        super().__init__(message=f"Book with ISBN '{isbn}' already exists", status_code=409,)
class InvalidYearException(AppException):
    """invalid year"""
    def __init__(self, year: int):
        from datetime import datetime
        current_year = datetime.now().year
        super().__init__(message=f"Year {year} is invalid (must be 1000-{current_year})", status_code= 400,)
class InvalidPagesException(AppException):
    """invalid pages"""
    def __init__(self, pages: int):
        super().__init__(message=f"Pages count must be positive, got pages {pages}", status_code= 400,)
class OpenLibraryException(AppException):
    """open library"""
    def __init__(self, message: str):
        super().__init__(message=f"Open library API error: {message}", status_code=503,)
class OpenLibraryTimeoutException(AppException):
    """open library timeout"""
    def __init__(self, timeout: float):
        super().__init__(message=f"Open library API timeout after {timeout}s", status_code=504,)

