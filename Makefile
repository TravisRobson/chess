.PHONY: clean run test

run:
	time ./chess/main.py

test:
	pytest -v tests/

clean:
	rm -rf .pytest_cache
	rm -rf chess/__pycache__
	rm -rf tests/__pycache__