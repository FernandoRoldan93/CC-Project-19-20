# Herramienta de construcción

Para poder controlar la ejecución de los módulos o la instalación de los paquetes necesarios del sistema, necesitaremos una herramienta de construcción. En este caso, utilizaremos la ampliamente conocida [make](https://www.gnu.org/software/make/). Esta herramienta nos permitirá, a través del fichero [Makefile](../Makefile), definir una serie comandos que, asociados a una regla, se ejecutaran de forma sucesiva, haciendo así más clara y sencilla la ejecución del sistema de una forma correcta.

Para ello, se han definido dos reglas:

`make`: Instalación y creación de un entorno virtual de Python en el que se instalarán todos los paquetes necesarios para la ejecución del sistema.

`make test`: En este caso, esta regla nos sirve para ejecutar los tests sobre el sistema creado.

Mas adelante se añadirán reglas que solventen las diferentes necesidades que surjan en el sistema.


# Integración continua

Una buena práctica a la hora de realizar un sistema en la nube consiste en la utilización de herramientas de integración continua. Estas herramientas permitirán realizar test de integración para que cada vez que se realice un cambio en la aplicación podamos detectar los posibles fallos lo antes posible. Hoy en día podemos encontrar una gran variedad de herramientas de integración continua, como pueden ser [Jenkins](https://jenkins.io/) o [travis-ci](https://travis-ci.org/). En este caso, las herramientas que se han elegido son Travis-CI y [CircleCI](https://circleci.com/). Se han elegido debido al conocimiento sobre Travis del que ya disponía y a la facilidad que ambas nos ofrecen. Además de lo antes mencionado, también son ampliamente utilizadas en el ámbito del "Cloud Computing", lo que nos asegurará que hay gran cantidad de manuales y soluciones a posibles problemas.

Mediante el uso de Travis, también se ha comprobado para que versiones de Python es compatible el sistema. Estas versiones son todas las comprendidas entre la versión **3.5** y la versión **3.8** ambas incluidas.

Los ficheros de configuración de Travis y CircleCI se pueden consultar en los siguientes enlaces:
1. [Fichero de configuración de Travis](../.travis.yml)
2. [Fichero de configuración de CircleCI](../.circleci/config.yml)

Además de lo anterior, también se ha utilizado una herramienta de cobertura de código. Estas herramientas nos permiten conocer cual es la cantidad de código que hemos cubierto con tests. Esto último nos llevará a tener un código más libre de errores y de mejor calidad (sin redundancias, por ejemplo). La herramienta que se utilizará por tanto es [codecov](https://codecov.io/).

El estado de la aplicación en las tres plataformas se puede comprobar en la cabecera del documento [README](../README.md), en este se han incluido los badges de las tres plataformas.
