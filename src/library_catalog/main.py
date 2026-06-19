"""
Library Catalog API - Точка входа приложения.
"""

from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .external.openlibrary.client import OpenLibraryClient
from .core.config import settings, Settings, get_settings
from .core.database import dispose_engine
from .core.exceptions import register_exception_handlers
from .core.logging_config import setup_logging
from .api.v1.routers import books, health


# ========== LIFECYCLE EVENTS ==========

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifecycle manager для FastAPI.

    Выполняется при:
    - startup: настройка логирования
    - shutdown: закрытие подключений к БД
    """
    # Startup
    setup_logging()
    settings = get_settings()

    app.state.ol_client = OpenLibraryClient(
        base_url=settings.openlibrary_base_url,
        timeout=settings.openlibrary_timeout
    )

    yield


    if hasattr(app.state.ol_client, '_client'):
        await app.state.ol_client._client.aclose()


# ========== CREATE APP ==========
def create_app(settings: Settings | None = None) -> FastAPI:
    """Фабрика для создания экземпляра FastAPI"""
    # Если настройки не передали (как при запуске uvicorn), берем стандартные
    cfg = settings or get_settings()
    app = FastAPI(title="Library Catalog API", lifespan=lifespan)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=cfg.cors_origins,
        allow_credentials=True,
        allow_methods=['GET', 'POST', 'PATCH', 'DELETE'],
        allow_headers=['Authorization', 'Content-Type'],
    )

    return app

app = create_app()


# ========== EXCEPTION HANDLERS ==========

register_exception_handlers(app)

# ========== ROUTERS ==========

# Версия 1 API
app.include_router(
    books.router,
    prefix=settings.api_v1_prefix,
)
app.include_router(
    health.router,
    prefix=settings.api_v1_prefix,
)

# ========== ROOT ENDPOINT ==========

@app.get("/")
async def root():
    """Корневой эндпоинт."""
    return {
        "message": "Welcome to Library Catalog API",
        "docs": settings.docs_url,
        "version": "1.0.0",
    }


# ========== RUN ==========

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug,
    )