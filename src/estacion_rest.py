# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán
"""

import os
import json
from stationbd import StationBD
from flask import Flask, Response, request

app = Flask(__name__)
estaciones = StationBD()

def estacion_to_dict(estacion):
    estacion_dictionary = {
    "id": estacion.id,
    "Direccion": estacion.direccion,
    "Numero de puestos": estacion.nPuestos,
    "Numero de puestos libres": estacion.puestos_libres
    }
    return estacion_dictionary

def bicicleta_to_dict(bicicleta):
    raise NotImplementedError

@app.route("/", methods=['GET'])
def index():
    return Response("Enhorabuena, has encontrado la pagina principal del microservicio de gestion de estaciones.", status = 200)

@app.route("/aniadir_estacion/<int:id>/<dir>/<int:n_puestos>", methods=['PUT'])
def aniadir_estacion(id, dir, n_puestos):
    return estaciones.aniadir_estacion(id, dir, n_puestos)

@app.route("/estacion/<int:id>", methods=['GET'])
def get_estacion(id):
    estac = estaciones.get_estacion_by_id(id)
    if estac != None:
        estac_dict = estacion_to_dict(estac)
        return Response(json.dumps(estac_dict), status=200, mimetype="application/json")
    else:
        return "No hay ninguna estacion con ese ID"
