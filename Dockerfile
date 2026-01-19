FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1
ENV UV_NO_DEV=1

WORKDIR /opt/telegram-bot

COPY pyproject.toml uv.lock ./

RUN apt-get update
COPY --from=ghcr.io/astral-sh/uv:0.9.25 /uv /uvx /bin/

RUN uv sync --locked --no-install-project

COPY src ./

CMD ["uv", "run", "python", "main.py"]