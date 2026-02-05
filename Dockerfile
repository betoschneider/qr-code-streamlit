FROM python:3.12-slim

# Instalar uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Ativar otimizações do uv (bytecode compilation)
ENV UV_COMPILE_BYTECODE=1

# Impedir que o uv instale pacotes no diretório de cache do sistema
ENV UV_LINK_MODE=copy

# Copiar arquivos de configuração do uv
COPY pyproject.toml uv.lock ./

# Instalar dependências (sem o projeto em si, se for o caso, ou use --no-install-project)
# Usando sync para garantir que o ambiente seja idêntico ao lockfile
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev

# Copiar arquivos da aplicação
COPY app.py .

# Garantir que o ambiente virtual criado pelo uv seja usado
ENV PATH="/app/.venv/bin:$PATH"

# Expor porta
EXPOSE 8515

# Configurar Streamlit
ENV STREAMLIT_SERVER_PORT=8515
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0
ENV STREAMLIT_SERVER_HEADLESS=true

# Executar a aplicação usando o venv
CMD ["streamlit", "run", "app.py"]
