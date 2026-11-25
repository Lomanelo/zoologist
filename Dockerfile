  FROM python:3.12-trixie
  COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
  WORKDIR /app
  ENV UV_NO_DEV=1


  COPY pyproject.toml uv.lock README.md ./
  COPY src/ ./src/
  COPY api/ ./api/
  COPY models/ ./models/

  RUN uv sync --frozen

  CMD ["uv", "run", "uvicorn", "api.fast:app", "--host", "0.0.0.0", "--port", "8080"]
