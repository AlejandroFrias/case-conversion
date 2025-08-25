.DEFAULT_GOAL := help
VENV = .venv
DIST = dist

.PHONY: help
help:
	@echo "'make test lint' for testing and linting."

$(VENV)/bin/activate: pyproject.toml
	uv sync

.PHONY: setup
setup:
	uv sync

.PHONY: lint
lint: $(VENV)/bin/activate
	$(VENV)/bin/ruff check

.PHONY: format
format: $(VENV)/bin/activate
	$(VENV)/bin/ruff check --fix

.PHONY: tc
tc: $(VENV)/bin/activate
	$(VENV)/bin/ty check

.PHONY: test
test: $(VENV)/bin/activate
	$(VENV)/bin/coverage run -m pytest --doctest-modules && $(VENV)/bin/coverage report

.PHONY: coverage-badge
coverage-badge:
	$(VENV)/bin/coverage-badge -f -o coverage.svg

.PHONY: clean
clean:
	rm -rf **/__pycache__
	rm -rf .venv
	rm -rf .coverage
	rm -rf .pytest_cache

.PHONY: build
build:
	uv build

.PHONY: upload
upload:
	uv run twine check $(DIST)/* && uv run twine upload $(DIST)/*