#Servicio de busqueda para realizar clases

###Autor: Fernando Roldán Zafra

##Descripción:
Hoy en día debido a la gran intercomunicación y globalización el la que vivimos, cualquier persona puede tener habilidades muy diversas. Estas habilidades pueden ir desde tocar el piano, hasta hablar un idioma extranjero o realizar algun tipo de manualidad. Sin embargo, a la hora de aprender alguna habilidad nos encontramos con el problema de que dependiendo de cual sea puede resultarnos muy cara o muy dificil de encontrar un buen profesor a nuestro alrededor.

##Solución

Para resolver este problema se propone una plataforma la cual nos permita intercomunicar a todas esas personas que tienen alguna habilidad que los hace especiales y quieren aprender alguna otra habilidad de forma gratuita. Realizandose así un intercambio de habilidades, siendo cada uno de los participantes en profesor y alumno a la vez.

Para ello, cada uno de los usuarios se registrará en la plataforma especificando que habilidades poseen, cuales quieren aprender.

##Arquitectura

Para realizar este sistema se pretende realizar un despliege en la nube basandonos en una arquitectura basada en microservicios. Esta arquitectura nos permitira una gran escalabilidad y una funcionalidad modular, pudiendo desplegar los microservicios de forma independiente.

Se definiran los siguientes microservicios:

- Gestion de usuarios.
- Base de datos.
- Busqueda de personas segun habilidades compatibles.

Adicionalmente a los anteriores se desarrollará un microservicio que gestione los logs de los anteriores.

##Especificacion de microservicios

Para la implementación de todos estos microservicios se usará **Python** por la gran cantidad de librerias disponibles y para la base de datos se creara una base de datos [**MongoDB**](https://www.mongodb.com/es).

Por otro lado, para realizar la API REST se usara [**Flask**](https://palletsprojects.com/p/flask/) debido a la gran facilidad que ofrece a principiantes en este framework.

Por otra parte se desarrollará un broker basado en [**RabbitMQ**](https://www.rabbitmq.com/) para la comunicación directa entre los microservicios.