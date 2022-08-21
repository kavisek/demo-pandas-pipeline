# enviroment variables are
PROJECT_ID=kavi-dummy-project-123

.PHONY: install
install:
	poetry install

.PHONY: build
build: install
	poetry build

.PHONY: black
black:
	poetry run black .

.PHONY: pytest
pytest:
	poetry run pytest --cov=./tests --black -rAP 

.PHONY:black
black:
	isort