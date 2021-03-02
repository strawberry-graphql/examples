install:
	poetry install && PYTHONPATH=src poetry run ./manage.py migrate

install-postgres:
	poetry install -E postgres && PYTHONPATH=src poetry run ./manage.py migrate

run:
	PYTHONPATH=src poetry run uvicorn demo.asgi:application --reload --debug --reload-dir src
