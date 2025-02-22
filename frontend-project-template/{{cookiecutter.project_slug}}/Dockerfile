FROM python:{{ cookiecutter.python_min_version }}-slim

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 test=test COVERAGE_FILE=/app/.coverage

RUN mkdir /app \
    && apt-get update \
    && apt-get install -y --no-install-recommends unzip curl gcc \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r app \
    && useradd -r -m -g app app

RUN pip install --upgrade --no-cache-dir pip uv

COPY pyproject.toml uv.lock /app/

WORKDIR /app
RUN uv sync

COPY . /app

RUN chmod +x -R /app \
    && chown -R app:app /app

USER app
EXPOSE 8501
WORKDIR /app/

ENV PYTHONPATH=src
ENTRYPOINT ["uv", "run", "python", "-m", "streamlit", "run", "src/frontend/app.py"]