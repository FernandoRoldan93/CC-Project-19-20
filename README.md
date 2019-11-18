# Proyecto para la asignatura de Cloud Computing (UGR)

### Autor: Fernando Roldán Zafra

## Descripción:
Se propone desarrollar un sistema llamado "CityByke", este sistema consiste en un sistema de gestión de bicicletas de alquiler en la ciudad. En este sistema un gestor podrá organizar todo lo relacionado con el alquiler de las mismas a través de la nube.

## Arquitectura

Este sistema se implementará siguiendo una arquitectura basada en microservicios. Para mas información acerca de los diferentes microservicios y componentes del sistema se puede consultar la [página](docs/arquitectura.md) destinada a tal efecto.

Por otra parte, se ha realizado un estudio de las diferentes entidades que formaran parte de este problema. Estas entidades surgen del [análisis](https://github.com/FernandoRoldan93/CC-Project/blob/master/doc/DDD_analisis.md) basado en el diseño guiado por el dominio (DDD, [Domain-Driven Design](https://en.wikipedia.org/wiki/Domain-driven_design)).

Hay que destacar que el lenguaje que se utilizará para la realización de este proyecto, será [Python](https://www.python.org/) por la gran cantidad de facilidades que nos ofrece en cuanto a módulos y a herramientas se refiere.

## Herramienta de construcción

Como herramienta de construcción utilizaremos la ampliamente conocida makefile.
