.PHONY: test

test:
	pytest

code_coverage:
	pytest --cov=lib
