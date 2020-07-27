# Herramienta de construcción

    buildtool: Makefile

Como herramienta de construcción utilizaremos la ampliamente conocida [Make](https://www.gnu.org/software/make/). La elección de esta herramienta y no de otras herramientas de construcción como [Scons](https://github.com/SCons/scons), se debe principalmente a que ya disponía de conocimientos de esta herramienta y aunque Scons es tremendamente fácil de usar, se encuentra menos extendida que Make. Además de esto, esta última herramienta ofrece todas las utilidades que necesitaremos en el proyecto de forma muy simple.

En cuanto a las utilidades que ofrece Make, esta herramienta nos permitirá, a través del fichero [Makefile](./Makefile), realizar varias opciones de forma automática como son la instalación y el testeo de los microservicios desarrollados. Para este propósito se han definido 2 comandos que se ejecutaran utilizando las siguientes ordenes:

	make install
Mediante la ejecución de esta orden se instalarán primero todas las dependencias necesarias del proyecto. Primero se instalará [Pipenv](https://pipenv-es.readthedocs.io/es/latest/), el cual nos servirá para crear un entorno virtual de Python en la versión **3.7**. Una vez se ha instalado dicho entorno, se inicializa y se hace una instalación en el entorno de todos los paquetes presentes en el fichero [requirements.txt](./requirements.txt) el cual puede ser consultado para conocer que paquetes se instalarán.

	make test
En este caso, se ejecutarán todos los test del proyecto. Por un lado se realizan los tests unitarios con [pytest](https://pypi.org/project/pytest/) y más tarde se realizarán los test de cobertura con [codecov](https://docs.codecov.io/docs). La cobertura de código puede consultarse en el badge destinado a tal efecto de esta página o mediante este [enlace](https://codecov.io/gh/FernandoRoldan93/CC-Project).
