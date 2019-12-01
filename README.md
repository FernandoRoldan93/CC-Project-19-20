# Proyecto para la asignatura de Cloud Computing (UGR)
[![Build Status](https://travis-ci.org/FernandoRoldan93/CC-Project.svg?branch=master)](https://travis-ci.org/FernandoRoldan93/CC-Project)
[![codecov](https://codecov.io/gh/FernandoRoldan93/CC-Project/branch/master/graph/badge.svg)](https://codecov.io/gh/FernandoRoldan93/CC-Project)
[![CircleCI](https://circleci.com/gh/FernandoRoldan93/CC-Project.svg?style=svg)](https://circleci.com/gh/FernandoRoldan93/CC-Project)
### Autor: Fernando Roldán Zafra

## Descripción:
Se propone desarrollar un sistema llamado "CityByke", este sistema consiste en un sistema de gestión de bicicletas de alquiler en la ciudad. En este sistema un gestor podrá organizar todo lo relacionado con el alquiler de las mismas a través de la nube.

## Arquitectura

Este sistema se implementará siguiendo una arquitectura basada en microservicios. Para mas información acerca de los diferentes microservicios y componentes del sistema se puede consultar la [página](doc/arquitectura.md) destinada a tal efecto.

Por otra parte, se ha realizado un estudio de las diferentes entidades que formaran parte de este problema. Estas entidades surgen del [análisis](https://github.com/FernandoRoldan93/CC-Project/blob/master/doc/DDD_analisis.md) basado en el diseño guiado por el dominio (DDD, [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design)).

Hay que destacar que el lenguaje que se utilizará para la realización de este proyecto, será [Python](https://www.python.org/) por la gran cantidad de facilidades que nos ofrece en cuanto a módulos y a herramientas se refiere.

## Herramienta de construcción

Como herramienta de construcción utilizaremos la ampliamente conocida [make](https://www.gnu.org/software/make/). Esta herramienta nos permitirá, a través del fichero [Makefile](./Makefile), realizar varias opciones de forma automática. Para este propósito se han definido 2 comandos que se ejecutaran utilizando las siguientes ordenes:

`make install` o `make`: Cualquiera de estas dos ordenes crearan un entorno virtual de Python e instalarán en el las dependencias necesarias.

`make test`: En este caso, este comando nos permitirá realizar todos los tests desarrollados.

## Tests y herramientas de integración continua

  buildtool: Makefile

Para poder llevar un correcto control del proyecto se han desarrollado varios tests sobre los microservicios implementados. Esto permitirá comprobar que el sistema funciona correctamente después de realizar algún cambio. Para realizar estas comprobaciones se ha elegido utilizar el método de integración continua en la nube. De esta forma se crearan entornos virtuales en la nube donde se ejecutará el sistema en varias versiones de Python.

Las herramientas de integración continua que se han utilizado son [travis](https://travis-ci.org/) y [CircleCI](https://circleci.com/). Se han elegido debido al conocimiento sobre travis del que ya disponía y debido a la facilidad que ambas nos ofrecen.

Por otro lado, también se ha integrado una herramienta de cobertura de código, esta es [codecov](https://codecov.io/). Esta herramienta nos permitirá comprobar cual es el porcentaje de código cubierto por nuestros tests.
