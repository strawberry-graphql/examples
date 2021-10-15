FROM python:3.9-slim-buster

RUN mkdir /app

COPY /reddit /migrations /app/
COPY /pyproject.toml /poetry.lock /app/

WORKDIR /app

RUN pip install poetry
RUN poetry install

ENTRYPOINT [ "poetry", "run", "uvicorn", "reddit:app" ]
