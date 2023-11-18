FROM python:3.9-slim
LABEL maintainer="Aryan Iyappan <aryaniyappan2006@gmail.com>"

ARG APP_HOME=/app/
WORKDIR ${APP_HOME}

# install poetry
RUN pip install poetry

# install dependencies
COPY ./poetry.lock ./pyproject.toml ${APP_HOME}
RUN poetry install --no-dev

# copy project files
COPY ./ ${APP_HOME}
