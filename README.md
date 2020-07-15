# Proyecto para la asignatura de Cloud Computing (UGR)
[![Build Status](https://travis-ci.org/FernandoRoldan93/CC-Project.svg?branch=master)](https://travis-ci.org/FernandoRoldan93/CC-Project)
[![codecov](https://codecov.io/gh/FernandoRoldan93/CC-Project/branch/master/graph/badge.svg)](https://codecov.io/gh/FernandoRoldan93/CC-Project)
[![CircleCI](https://circleci.com/gh/FernandoRoldan93/CC-Project.svg?style=svg)](https://circleci.com/gh/FernandoRoldan93/CC-Project)

### Autor: Fernando Roldán Zafra

## Indice General
- [Entidades del sistema](./doc/DDD_analisis.md)
- [Arquitectura](./doc/arquitectura.md)
- [Herramienta de construcción e integración continua](./doc/buildtool_integracion_continua.md)
- [Frameworks y herramientas](./doc/Frameworks_herramientas.md)

## Descripción:
Hoy en día el cambio climático supone un serio problema y una de las causas de este problema es la movilidad urbana. Una solución a este problema consiste en la utilización de transportes limpios, como la bicicleta, en la ciudad. Sin embargo, hay que proveer a la población de dichas bicicletas, para ello cada vez más se ven en las ciudades estaciones de alquiler de bicicletas. Este servicio permite al cliente alquilar durante una determinada distancia o tiempo una bicicleta, la cual deberá ser devuelta a una estación tras su uso.
Para poder llevar a cabo toda esta actividad se necesita un sistema de gestión. Se propone desarrollar un sistema llamado "CityBike" para realizar esta actividad. Este sistema se propone realizar una gestión centralizada de todo lo relacionado con los servicios de alquiler de bicicletas en una ciudad facilitando así todo el trabajo de gestión a través de la nube.

## Arquitectura

Este sistema se implementará siguiendo una arquitectura basada en microservicios. Para más información acerca de los diferentes microservicios y componentes del sistema se puede consultar la [página](doc/arquitectura.md) destinada a tal efecto.

Por otra parte, se ha realizado un estudio de las diferentes entidades que formaran parte de este problema. Estas entidades surgen del [análisis](./doc/DDD_analisis.md) basado en el diseño guiado por el dominio (DDD, [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design)).

## Herramienta de construcción

    buildtool: Makefile

Como herramienta de construcción utilizaremos la ampliamente conocida [make](https://www.gnu.org/software/make/). Esta herramienta nos permitirá, a través del fichero [Makefile](./Makefile), realizar varias opciones de forma automática. Para este propósito se han definido 2 comandos que se ejecutaran utilizando las siguientes ordenes:

`make install` o `make`: Cualquiera de estas dos ordenes crearan un entorno virtual de Python e instalarán en el las dependencias necesarias.

`make test`: En este caso, este comando nos permitirá realizar todos los tests desarrollados.

## Tests y herramientas de integración continua

Para poder llevar un correcto control del proyecto se han desarrollado varios tests sobre los microservicios implementados. Esto permitirá comprobar que el sistema funciona correctamente después de realizar algún cambio. Para realizar estas comprobaciones se ha elegido utilizar el método de integración continua en la nube. De esta forma se crearán entornos virtuales en la nube donde se ejecutará el sistema en varias versiones de Python.

Las herramientas de integración continua que se han utilizado son [travis](https://travis-ci.org/) y [CircleCI](https://circleci.com/). Para saber sobre estas herramientas y como se han incluido en el proyecto, se puede consultar el enlace del indice a la sección correspondiente o a traves de este [enlace](./doc/buildtool_integracion_continua.md)
