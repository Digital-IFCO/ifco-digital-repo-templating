FROM python:{{cookicutter.python_min_version}}-slim

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 test=test COVERAGE_FILE=/app/.coverage
ENV POETRY_VIRTUALENVS_CREATE=false

RUN mkdir /app \
    && apt-get update \
    && apt-get install -y --no-install-recommends unzip curl gcc \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd -r app \
    && useradd -r -m -g app app \
    && pip install --upgrade --no-cache-dir pip \
    && pip install --no-cache-dir poetry==1.5.1

COPY pyproject.toml poetry.lock /app/

RUN cd /app \
    && poetry install --with dev --no-root

COPY . /app
RUN chmod +x -R /app \
    && chown -R app:app /app \
    && cd /app \
    && poetry install --only-root

USER app

EXPOSE 8501

WORKDIR /app/src/frontend/

ENTRYPOINT ["streamlit", "run", "app.py"]
