#Instalación de todos los paquetes necesarios.
install:
	#Instalación de la herramienta de creación de entornos virtuales de Python
	pip install pipenv
	#Instalacion y creación de un entorno virtual.
	pipenv install --python 3.7
	#Dentro de dicho entorno, instalamos todos los paquetes definidos en el archivo
	#requirements.txt
	pipenv run pip install -r requirements.txt

#Realización de tests
test:
	#Testeo de las clases de estacion
	pipenv run python -m pytest tests/test_estacion.py
	#Testeo de las clases de bicicleta
	pipenv run python -m pytest tests/test_bicicletas.py

	#Test de cobertura de la clase estacion y bicicletas
	pipenv run python -m pytest --cov=estacion --cov=bicicleta --cov=stationbd --cov=bikebd tests/

#Levantar Microservicios
start:
	pipenv run gunicorn --chdir src estacion_rest:app -b :${PORT} -p pid_estaciones.pid --daemon

stop:
	pipenv run kill `cat src/pid_estaciones.pid`
