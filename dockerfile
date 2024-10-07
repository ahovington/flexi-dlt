FROM python:3.11-slim-bullseye

RUN apt-get update && \
    apt-get install -y gcc libpq-dev

COPY --from=ghcr.io/astral-sh/uv:0.4.0 /uv /bin/uv

WORKDIR /app

COPY --from=root pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --all-extras

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT ["uv", "run", "-m", "entrypoint"]