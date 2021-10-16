FROM python:3.9-slim
LABEL maintainer="Aryan Iyappan <aryaniyappan2006@gmail.com>"

WORKDIR /app

# install poetry
RUN pip install poetry

# install dependencies
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --no-dev

# copy project files
COPY ./ ./
