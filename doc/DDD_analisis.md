# Análisis DDD: Entidades

Este proyecto se puede dividir en dos claras entidades: 

* La primera de ellas no puede ser otra que la entidad "Bicicleta", todo el sistema girará en torno a esta entidad y es que en la mayoría de los casos realizaremos peticiones al sistema enfocándonos en las bicicletas. Las bicicletas en nuestro sistema constarán de una serie de propiedades, por ejemplo, su estado (disponible o ocupada), su fecha de incorporación al sistema, una lista de los ultimos usuarios que la han usado, un histórico de las ultimas estaciones donde se a depositado... Por lo tanto el microservicio que se encargará de esta entidad nos permitirá realizar una serie de operaciones sobre ella, como pueden ser la consulta del estado de una bicicleta o la retiración o incorporación de una nueva. 

* Por otro lado contamos tambien con la entidad "Estación", esta se centrará en la gestión de las diferentes estaciones de las que dispondremos en nuestro sistema. Una estación es el lugar donde los usuarios depositarán y recogeran las bicicletas. Ademas de esto la estación proveerá de información como el numero de bicicletas disponibles en ella o la identificación de cada una de las bicicletas que se encuentran allí depositadas. Este microservicio nos proveera de información como la antes mencionada y ademas nos permitira realizar diversas operaciones sobre las estaciones como pueden ser la creación de una nueva estación, eliminación de una existente o gestión de las bicicletas que se pueden retirar o no de una estación.


