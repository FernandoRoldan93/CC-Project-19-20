# Frameworks y lenguaje de programación

Para realizar todo el proyecto se han tenido que tomar varias decisiones en cuanto a que herramientas y lenguajes utilizar. Primero hablaremos del lenguaje de programación.

## Lenguaje
Tras valorar varias opciones de lenguajes como Python, Java o Ruby se ha elegido finalmente realizar el proyecto en Python. Algunas de las razones por las cuales se ha desarrollado el proyecto en este lenguaje son las siguientes:

 - Conocimiento previo en dicho lenguaje.
 - Gran cantidad de módulos y paquetes disponibles para dicho lenguaje.
 - Una enorme comunidad de desarrolladores en dicho lenguaje.
 - Posibilidad de incluir técnicas de Machine Learning en el proyecto de forma fácil si surgiera la necesidad.

De todas estas razones hay que detallar la posibilidad de incluir técnicas de machine learning en el proyecto. Esto último, aunque no forma parte de los objetivos del proyecto es una posibilidad a tener en cuenta y es que una vez se disponga de datos de uso del sistema se podría incorporar alguna de estas técnicas de forma fácil y sin necesidad de reestructurar el proyecto. En caso de ser así y como se puede ver [aquí](https://becominghuman.ai/best-languages-for-machine-learning-in-2020-6034732dd242) Python es el mejor lenguaje para dicho propósito. De tal forma, esta última razón no es más que una proyección de futuro, sin constituirse como un objetivo a desarrollar para el cumplimiento de la asignatura y del proyecto.

## Frameworks para desarrollo.
En este proyecto necesitaremos varias herramientas para poder desarrollar el sistema. En esta sección se pretende detallar las herramientas que se utilizarán y el motivo por el cual se han elegido. Según el esquema de la arquitectura del proyecto presente en el siguiente [fichero](./arquitectura.md) se pueden diferenciar diferentes entidades o estructuras para las cuales serán necesarias las herramientas que se detallan a continuación:

- Como framework para el desarrollo de la API REST se han barajado diversas opciones como [flask](https://flask.palletsprojects.com/en/1.1.x/), [Falcon](https://falcon.readthedocs.io/en/stable/), [Tornado](https://www.tornadoweb.org/en/stable/) o [FastAPI](https://fastapi.tiangolo.com/). Sin embargo, a pesar de que cualquiera de estas opciones es válida se ha optado por utilizar Flask. Los motivos principales de esta decisión se basan en que se trata de una herramienta tremendamente extendida y de fácil aprendizaje. Además de esto, ya disponía de algunos conocimientos previos sobre su utilización. 

- Para la herramienta de Logging se han barajado dos opciones: El módulo de [logging](https://docs.python.org/2/library/logging.html) de Python y [Loguru](https://loguru.readthedocs.io/en/stable/index.html). Tras investigar las posibles ventajas e inconvenientes de ambas opciones se ha decidido utilizar la herramienta de logging propia de Python. Esta decisión se ha tomado debido a que aún a pesar de que Loguru es muy fácil de aprender y de usar no se diferencia demasiado de la herramienta propia de Python. Y dado que es necesario instalar un paquete adicional, como es la herramienta en sí, se ha preferido utilizar la herramienta de logging de python.
