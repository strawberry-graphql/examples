FROM python:3.9

WORKDIR /app

# install poetry
RUN pip install poetry

# install dependencies
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install

# copy project files
COPY ./ ./

CMD [ "poetry", "run", "uvicorn", "reddit:app", "--host=0.0.0.0" ]
