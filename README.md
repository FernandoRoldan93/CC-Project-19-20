# Proyecto para la asignatura de Cloud Computing (UGR)

### Autor: Fernando Roldán Zafra

## Descripción:
Se propone desarrollar un sistema llamado "CityByke", este sistema consiste en un sistema de gestión de bicicletas de alquiler en la ciudad. En este sistema un gestor podrá organizar todo lo relacionado con el alquiler de las mismas a traves de la nube.

## Arquitectura

Este sistema se implementará siguiendo una arquitectura basada en microservicios. Se elige esta arquitectura debido al caracter del problema donde la lógica de negocio se encuentra bien separada. Ademas de esto, esta arquitectura nos aportara una serie de ventajas con respecto a la arquitectura monolitica, como puede ser, entre otras, que los cambios en los distintos microservicios no afectan al resto, pudiendo hacer actualizaciones en dichos microservicios de forma mas sencilla.

## Microservicios
Para definir los diferentes microservicios podemos fijarnos en el analisis de las diferentes entidades obtenidas a partir de un analisis basado en el diseño guiado por el dominio (DDD, [Domain-Driven Design](en.wikipedia.org/wiki/Domain-driven_design)). Los diferentes microservicios que obtenemos de este análisis son: 

* BikeManager: Este microservicio será el encargado de implementar todas las funciones relacionadas con la entidad "bicicleta".

* StationManager: Este microservicio será el encargado de gestionar la entrada y salida de bicicletas en la estación. Ademas de esto tambien se encargará de informar del numero de puestos libres y bicicletas disponibles en una estación especifica.

## Servicios
Ademas de los microservicios anteriormente mencionados se incluiran varios servicios que serán de utilidad para gestionar el sistema.

* Primero habrá que incluir un servicio que nos permita realizar todo el logging del sistema de forma centralizada, esto nos permitirá conocer los errores que pueden haber ocurrido en nuestro sistema a la vez que recogemos datos de actividad.

* Por otro lado necesitaremos un sistema de configuración distribuido para poder llevar un control centralizado del estado de cada uno de los microservicios a la vez que realizamos las configuraciones necesarias.

* Tambien necesitaremos una API Gateway para la comunicación entre los diferentes microservicios.

