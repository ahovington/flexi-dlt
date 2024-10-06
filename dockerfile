FROM ghcr.io/astral-sh/uv:python3.11-bookworm

WORKDIR /app

COPY pyproject.toml ./

RUN uv pip install -r pyproject.toml

COPY entrypoint ./entrypoint/
COPY --chown=appuser:appuser .dlt/ ./.dlt/

ENTRYPOINT ["uv", "run", "-m", "entrypoint"]
