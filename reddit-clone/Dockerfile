FROM python:3.9-slim

WORKDIR /app

# install poetry
RUN pip install poetry

# install dependencies
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install

# copy project files
COPY ./ ./

EXPOSE 8000

CMD poetry run uvicorn reddit:app --host=0.0.0.0
