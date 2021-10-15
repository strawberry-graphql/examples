FROM python:3.9

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock /app/

RUN pip install poetry
RUN poetry install

COPY ./reddit /app/reddit/

CMD [ "poetry", "run", "uvicorn", "reddit:app" ]
