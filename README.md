# Library Catalog API

REST API для управления библиотечным каталогом. Построен на современном стеке Python с акцентом на качество кода, асинхронность и чистую архитектуру.

## ✨ Особенности

- ⚡ **Асинхронность** — полностью async стек (FastAPI + SQLAlchemy)
- 📝 **Автодокументация** — Swagger UI и ReDoc из коробки
- 🧱 **Чистая архитектура** — разделение на API, Domain, Data слои
- 🐘 **PostgreSQL** — production-ready СУБД
- 🛠 **Инструменты качества** — Ruff, Mypy, Pytest
- 🐳 **Контейнеризация** — готовый docker-compose для БД
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

# 📚 API документация
# После запуска сервера документация доступна по адресам:

Swagger UI: http://localhost:8000/docs

ReDoc: http://localhost:8000/redoc

# 🏗️ Архитектура
# Проект построен на многослойной архитектуре:

API Layer → Domain Layer → Data Layer → Database

API Layer — эндпоинты и Pydantic схемы

Domain Layer — бизнес-логика и сервисы

Data Layer — репозитории и SQLAlchemy модели

# 👨‍💻 Разработка

# Запустить тесты
poetry run pytest

# Проверить типы
poetry run mypy src/

# Запустить линтер
poetry run ruff check src/

# Отформатировать код
poetry run ruff format src/
