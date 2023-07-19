dev:
	flask run --debug --reload

load:
	@echo "Loading data into database..."
	@python3 main.py

test:
	@python3 -m unittest tests/test_load.py