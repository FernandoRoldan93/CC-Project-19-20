# Herramienta de construcción

Para poder controlar la ejecución de los módulos o la instalación de los paquetes necesarios del sistema, necesitaremos un herramienta de construcción, en este caso, utilizaremos la ampliamente conocida [make](https://www.gnu.org/software/make/). Esta herramienta nos permitirá, a través del fichero [Makefile](../Makefile), definir una serie comandos que, asociados a una regla, se ejecutaran de forma sucesiva haciendo mas amena y comprensible la ejecución del sistema.

Para ello, se han definido dos reglas:

`make install`: Esta regla nos servirá para instalar y crear un entorno virtual de Python en el que se instalaran todos los paquetes necesarios para la ejecución del sistema.

`make test`: En este caso, esta regla nos sirve para ejecutar los tests sobre el sistema creado.

Conforme se vaya desarrollando el proyecto, se irán añadiendo más reglas.
