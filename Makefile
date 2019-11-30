install:
	pipenv install --three
	pipenv run pip install -r requirements.txt

test:
	pipenv run python -m pytest tests/test_bicicletas.py
	pipenv run python -m pytest --cov=estacion tests/
	pipenv run python -m pytest --cov=bicicletas tests/
