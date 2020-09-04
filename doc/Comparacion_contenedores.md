# Despliegue de microservicios en contenedores
## Elección de la imagen base

Cuando queremos desplegar una aplicación en un contenedor, un aspecto muy relevante es la imagen base de dicho contenedor, ya que de dicha imagen dependerá el tamaño del contenedor y la velocidad del mismo. Dicho esto, teniendo en cuenta que la aplicación se esta desarrollando en Python una de las elecciones más lógicas es utilizar una imagen base de Python (las cuales se pueden encontrar [aquí](https://hub.docker.com/_/python)). Estas imágenes no son mas que instalaciones de Python en un sistema operativo junto con algunas herramientas útiles por lo que, a priori, serán livianos y sin mucha carga en herramientas que realmente no utilizaremos.

Dentro de todas las posibles opciones nos centraremos en las imágenes que parten de Python 3.7 ya que es la versión que hemos elegido para el proyecto. Como se puede ver en el enlace anterior, hay varias imágenes con la versión 3.7 pero como se puede ver en este [enlace](https://pythonspeed.com/articles/base-image-python-docker-images/), es preferible utilizar una imagen que utilice Debian, Ubuntu o centOS. Por lo tanto nos centraremos en probar las siguientes imágenes de base:
- [3.7-slim-stretch](https://github.com/docker-library/python/blob/fd177393414a3344bc7da6b1e06c981816143f92/3.7/stretch/slim/Dockerfile)
- [3.7-stretch](https://github.com/docker-library/python/blob/fd177393414a3344bc7da6b1e06c981816143f92/3.7/stretch/Dockerfile)
- [3.7-slim](https://github.com/docker-library/python/blob/fd177393414a3344bc7da6b1e06c981816143f92/3.7/buster/slim/Dockerfile)
- [3.7-buster](https://github.com/docker-library/python/blob/fd177393414a3344bc7da6b1e06c981816143f92/3.7/buster/Dockerfile)

Para realizar la prueba de estas imágenes se desplegará el contenedor con cada una de ellas y se medirán las prestaciones con ab testing para 1000 peticiones con un nivel de concurrencia de 100, los resultados se pueden ver a continuación:

|Imagen        |Tamaño  |Peticiones por segundo [#/sec]|Tiempo por petición medio [ms] |Tiempo total [sec]|
|--------------|--------|------------------------------|-------------------|-------------|
| slim-stretch | 123 MB | 2177.12                      | 45.9 ms           | 0.459       |
| stretch      | 928 MB | 2031.35                      | 49.2 ms           | 0.492       |
| slim         | 139 MB | 2187.54                      | 45.7 ms           | 0.457       |
| buster       | 903 MB | 2161.19                      | 46.2 ms           | 0.463       |

Llegados a este punto y viendo los resultados obtenidos en la tabla anterior, podemos observar que la mejor imagen para el proyecto es la imagen slim-stretch, tanto por su tamaño como por su rendimiento.

## Despliegue en Docker Hub
