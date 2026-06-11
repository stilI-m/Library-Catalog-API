Library Catalog API
REST API для управления библиотечным каталогом, построенный на современном стеке Python.

🚀 Технологии
FastAPI — современный асинхронный веб-фреймворк

SQLAlchemy 2.0 — асинхронная ORM

PostgreSQL — реляционная база данных

Alembic — миграции схемы БД

Pydantic V2 — валидация данных

Poetry — управление зависимостями

📦 Инструменты качества
Ruff — линтер и форматтер (быстрая замена flake8, isort, black)

Mypy — статическая типизация

Pytest — тестирование (unit + integration)

Pre-commit — автоматические проверки перед коммитом

🐳 Запуск
bash
# Клонировать репозиторий
git clone https://github.com/ваш-username/library-catalog-api
cd library-catalog-api

# Установить зависимости
poetry install

# Запустить PostgreSQL в Docker
docker-compose up -d

# Применить миграции
poetry run alembic upgrade head

# Запустить сервер
poetry run uvicorn src.library_catalog.main:app --reload
📚 API документация
После запуска сервера документация доступна по адресам:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

🏗️ Архитектура
Проект построен на многослойной архитектуре:

text
API Layer → Domain Layer → Data Layer → Database
API Layer — эндпоинты и Pydantic схемы

Domain Layer — бизнес-логика и сервисы

Data Layer — репозитории и SQLAlchemy модели

📁 Структура проекта
text
src/library_catalog/
├── api/           # Роутеры и Pydantic схемы
├── core/          # Конфигурация, логирование, исключения
├── data/          # Модели БД и репозитории
├── domain/        # Бизнес-логика и сервисы
└── external/      # Внешние API клиенты
👨‍💻 Разработка
bash
# Запустить тесты
poetry run pytest

# Проверить типы
poetry run mypy src/

# Запустить линтер
poetry run ruff check src/

# Отформатировать код
poetry run ruff format src/
