# Establecemos la version base del contenedor. (Estudio comparativo de imagenes base en la documentacion del proyecto)
FROM python:3.7-slim-stretch

# Definimos un argumento para la creacion del contenedor, este sera el puerto a traves del
# cual se podrá acceder al contenedor
ARG PORT

# Asignamos dicho puerto a la variable de entorno
ENV PORT=${PORT}

# Establecemos el directorio de trabajo
WORKDIR /Documentos/CC/CC-Project

# Copiamos al contenedor todos los archivos que necesitamos, incluyendo el archivo
# de requerimientos
COPY src/* ./
COPY docker_requirements.txt ./

# Actualizamos los paquetes del contenedor, incluido pip e instalamos los paquetes
# necesarios
RUN apt-get update && pip install --upgrade pip && pip install -r docker_requirements.txt

# Abrimos el puerto por el que se podrá acceder al servicio
EXPOSE ${port}

# Ejecutamos el servidor
CMD gunicorn --chdir . estacion_rest:app -b :${PORT}
