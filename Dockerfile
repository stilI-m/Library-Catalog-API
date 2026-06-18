FROM python:3.11-slim

WORKDIR /app

# 1. Устанавливаем самую свежую версию Poetry
RUN pip install poetry

# 2. Говорим Poetry: "Мы в Докере, не создавай виртуальное окружение"
RUN poetry config virtualenvs.create false

# 3. Копируем файлы конфигурации зависимостей
COPY pyproject.toml poetry.lock ./

# 4. Устанавливаем все библиотеки прямо в систему контейнера
RUN poetry install --no-root --no-interaction

# 5. Копируем весь остальной код проекта
COPY . .

# 6. Запускаем сервер
CMD ["uvicorn", "src.library_catalog.main:app", "--host", "0.0.0.0", "--port", "8000"]