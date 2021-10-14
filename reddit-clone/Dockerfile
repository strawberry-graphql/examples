FROM python:3.7

RUN mkdir /reddit

COPY /reddit /reddit
COPY /pyproject.toml /reddit

WORKDIR /reddit

RUN pip install poetry
RUN poetry install

ENTRYPOINT [ "poetry", "run", "uvicorn", "app" ]
