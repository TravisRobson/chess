.PHONY: clean pre-commit run test

pre-commit:
	pre-commit run --all-files

run:
	time ./chess/main.py

test:
	pytest -v tests/

clean:
	rm -rf .pytest_cache
	rm -rf chess/__pycache__
	rm -rf tests/__pycache__