# Library Catalog API

REST API для управления библиотечным каталогом. Построен на современном стеке Python с акцентом на качество кода, асинхронность и чистую архитектуру.

## ✨ Особенности

- ⚡ **Асинхронность** — полностью async стек (FastAPI + SQLAlchemy)
- 📝 **Автодокументация** — Swagger UI и ReDoc из коробки
- 🧱 **Чистая архитектура** — разделение на API, Domain, Data слои
- 🐘 **PostgreSQL** — production-ready СУБД
- 🛠 **Инструменты качества** — Ruff, Mypy, Pytest
- 🐳 **Контейнеризация** — готовый docker-compose для БД
## 🚀 Быстрый старт (через Docker)

Убедитесь, что у вас установлены Docker и Docker Compose.

```bash
# 1. Клонировать репозиторий
git clone https://github.com/stilI-m/Library-Catalog-API
cd library-catalog-api
  
# 2. Собрать и запустить контейнеры (База данных + API)
docker-compose up -d --build

# 3. Применить миграции для создания таблиц в БД
docker-compose exec app alembic upgrade head
```

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
```bash
poetry run pytest
```
# Проверить типы
```bash
poetry run mypy src/
```
# Запустить линтер
```bash
poetry run ruff check src/
```
# Отформатировать код
```bash
poetry run ruff format src/
```