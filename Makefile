#Instalación de todos los paquetes necesarios.
install:
	#Instalación de la herrmienta de creación de entornos virtuales de Python
	pip3 install pipenv
	#Instalacion y creación de un entorno virtual.
	pipenv install --three
	#Dentro de dicho entorno, instalamos todos los paquetes definidos en el archivo
	#requirements.txt
	pipenv run pip3 install -r requirements.txt

#Realización de tests
test:
	#Test de la clase "bicicletas"
	pipenv run python -m pytest tests/test_bicicletas.py
	#Test de cobertura de la clase estacion y bicicletas
	pipenv run python -m pytest --cov=estacion --cov=bicicletas tests/
