FROM python:3.9

WORKDIR /app

# First install poetry
RUN pip install poetry

# Then install dependencies
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install

COPY ./ ./

CMD [ "poetry", "run", "uvicorn", "reddit:app" ]
