.PHONY: build clean pre-commit run test

build:
	python3 -m pip install --upgrade build
	python3 -m build

clean:
	rm -rf .pytest_cache
	rm -rf chess.egg-info
	rm -rf dist
	rm -rf chess/__pycache__
	rm -rf tests/__pycache__

pre-commit:
	pre-commit run --all-files

run:
	time ./chess/main.py

test:
	pytest -v tests/
