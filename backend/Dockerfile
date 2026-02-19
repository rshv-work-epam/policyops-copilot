FROM python:3.11-slim
WORKDIR /app
COPY pyproject.toml ./
RUN pip install --upgrade pip && pip install .[test]
COPY app ./app
COPY alembic ./alembic
COPY alembic.ini ./
COPY scripts ./scripts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
