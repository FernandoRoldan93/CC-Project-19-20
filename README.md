# Proyecto para la asignatura de Cloud Computing (UGR)

### Autor: Fernando Roldán Zafra

## Descripción:
Se propone desarrollar un sistema llamado "CityByke", este sistema consiste en un sistema de gestión de bicicletas de alquiler en la ciudad. En este sistema un gestor podrá organizar todo lo relacionado con el alquiler de las mismas a través de la nube.

## Arquitectura

Este sistema se implementará siguiendo una arquitectura basada en microservicios. Se elige esta arquitectura debido al carácter del problema donde la lógica de negocio se encuentra bien separada debido a esto podemos diferenciar dos entidades que pueden trabajar independientemente la una de las otra. Estas entidades surgen del [análisis](https://github.com/FernandoRoldan93/CC-Project/blob/master/doc/DDD_analisis.md) basado en el diseño guiado por el dominio (DDD, [Domain-Driven Design](en.wikipedia.org/wiki/Domain-driven_design)).

Además de esto, esta arquitectura nos aportara una serie de ventajas con respecto a la arquitectura monolítica, como puede ser, entre otras, que los cambios en los distintos microservicios no afectan al resto, pudiendo hacer actualizaciones en dichos microservicios de forma más sencilla.

## Microservicios
Para definir los diferentes microservicios podemos fijarnos en el análisis mencionado anteriormente. Los diferentes microservicios que obtenemos de este análisis son: 

* `Bike`: Este microservicio será el encargado de implementar todas las funciones relacionadas con la entidad "bicicleta".

* `Station`: Este microservicio será el encargado de gestionar la entrada y salida de bicicletas en la estación. Además de esto también se encargará de informar del número de puestos libres y bicicletas disponibles en una estación especifica.

## Servicios
Además de los microservicios anteriormente mencionados se incluirán varios servicios que serán de utilidad para gestionar el sistema.

* Primero habrá que incluir un servicio que nos permita realizar todo el logging del sistema de forma centralizada, esto nos permitirá conocer los errores que pueden haber ocurrido en nuestro sistema a la vez que recogemos datos de actividad.

* Por otro lado necesitaremos un sistema de configuración distribuido para poder llevar un control centralizado del estado de cada uno de los microservicios a la vez que realizamos las configuraciones necesarias.

* También necesitaremos una API Gateway para la comunicación entre los diferentes microservicios.

