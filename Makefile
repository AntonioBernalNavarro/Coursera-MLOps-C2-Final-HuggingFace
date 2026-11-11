.PHONY: install test format lint container-lint refactor deploy all

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

format:
	black --check *.py mylib/*.py

lint:
	pylint --disable=R,C,missing-module-docstring,missing-function-docstring --ignore-patterns=test_.*?py *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	@echo "Deploy step placeholder - Skipping deployment for this lab."

all: install lint test format deploy