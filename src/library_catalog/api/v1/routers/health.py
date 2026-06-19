from fastapi import APIRouter, Depends
from fastapi import Response
from sqlalchemy import text

from ..schemas.common import HealthCheckResponse
from ...dependencies import DbSessionDep

router = APIRouter(prefix="/health", tags=["Health"])


@router.get(
    "/",
    response_model=HealthCheckResponse,
    summary="Health Check",
    description="Проверить состояние сервиса и подключение к БД",
    status_code=200,
)
async def health_check(db: DbSessionDep, response: Response):
    """
    Проверить здоровье сервиса.

    Проверяет:
    - Сервис запущен
    - Подключение к БД работает
    """
    # Простой запрос к БД
    try:
        await db.execute(text("SELECT 1"))
        db_status = "connected"
    except Exception:
        db_status = "disconnected"
        response.status_code = 503
    return HealthCheckResponse(
        status="healthy" if db_status == "connected" else "unhealthy",
        database=db_status,
    )