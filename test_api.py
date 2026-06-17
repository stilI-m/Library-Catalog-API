import asyncio
from src.library_catalog.external.openlibrary.client import OpenLibraryClient

async def main():
    client = OpenLibraryClient()
    print("Ищем книгу '1984' Джорджа Оруэлла...")

    # Дергаем наш метод enrich
    data = await client.enrich(title="1984", author="George Orwell")
    print("Результат из Open Library:", data)

    await client.close()

if __name__ == "__main__":
    asyncio.run(main())