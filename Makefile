install:
	pipenv install --three
	pipenv run pip install -r requirements.txt

test:
	pipenv run python -m pytest test/test_bicicletas.py
	pipenv run python -m pytest --cov=estacion test/
	pipenv run python -m pytest --cov=bicicletas test/
