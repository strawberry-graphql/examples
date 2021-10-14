FROM python:3.7

RUN mkdir /app

COPY /reddit /app
COPY /pyproject.toml /app

WORKDIR /app

RUN pip install poetry
RUN poetry install

ENTRYPOINT [ "poetry", "run", "uvicorn", "reddit:app" ]
