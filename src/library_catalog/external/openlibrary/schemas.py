from pydantic import BaseModel, Field

class OpenLibrarySearchDoc(BaseModel):
    """Document from search Open Library"""
    title:str
    autor_name:list[str] | None = Field(None, alias="author_name")
    cover_i: int| None = Field(None, alias="cover_i")
    subject:list[str] | None = None
    publisher:list[str] | None = None
    language:list[str] | None = None
    ratings_average: float | None = Field(None, alias="ratings_average")

    class Config:
        populate_by_name = True

class OpenLibrarySearchResponse(BaseModel):
    """Response from /search.json"""
    numFound:int
    docs:list[OpenLibrarySearchDoc]