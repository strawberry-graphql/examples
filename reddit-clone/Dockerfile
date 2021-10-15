FROM python:3.9-slim-buster

WORKDIR /app/

COPY ./poetry.lock ./pyproject.toml /app/

RUN pip install poetry
RUN poetry install

COPY ./reddit /app/reddit/

ENTRYPOINT [ "poetry", "run", "uvicorn", "reddit:app" ]
