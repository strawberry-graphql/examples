FROM python:3.9

ENV POETRY_VERSION=1.1.8 \
    # make poetry install to this location
    POETRY_HOME="/opt/poetry" \
    # make poetry create the virtual environment in the project's root
    # it gets named `.venv`
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    # do not ask any interactive question
    POETRY_NO_INTERACTION=1

RUN python -m pip install poetry

COPY ./pyproject.toml ./poetry.lock ./

RUN poetry install

COPY ./ ./

CMD poetry run uvicorn main:app --host 0.0.0.0
