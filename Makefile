all: lint test

test:
	poetry run pytest

lint:
	poetry run flake8 fizzbuzz.py test_fizzbuzz.py
