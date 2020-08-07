# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán
"""

import os
import json
from stationbd import StationBD
from bikebd import BikeBD
from flask import Flask, Response, request
import random

app = Flask(__name__)
estaciones = StationBD()
bicicletas = BikeBD()

def estacion_to_dict(estacion):
    estacion_dictionary = {
        "id": estacion.id,
        "Dirección": estacion.direccion,
        "Número de puestos": estacion.nPuestos,
        "Número de puestos libres": estacion.puestos_libres,
        "Bicicletas": tuple(bicicletas_to_dict(estacion.bicis))
    }
    return estacion_dictionary

def bicicletas_to_dict(bicicletas):
    bicis_list = []
    for bici in bicicletas:
        bici_dict = {}
        bici_dict = {
            "id": bici.id
        }
        bicis_list.append(bici_dict)
    return bicis_list

@app.route("/test_data")
def test_data():
    estaciones.aniadir_estacion(1, "Gonzalo Gallas", 3)
    estaciones.aniadir_estacion(2, "Facultad Informatica", 6)
    nombres = ["Paco", "Juan", "Javier", "Fernando", "Pablo", "Ruben"]
    for i in range(1, 10):
        bicicletas.aniadir_bici(i, 2020)
        for x in range(1, random.randint(2,4)):
            bicicletas.add_ultimo_usuario(i, nombres[random.randint(0,5)])
    for i in range(1,3):
        estaciones.depositar_bicicleta(estaciones.get_estacion_by_id(1),bicicletas.get_bici_by_id(i))
    for i in range(4,10):
        estaciones.depositar_bicicleta(estaciones.get_estacion_by_id(2),bicicletas.get_bici_by_id(i))
    return "Datos cargados con exito"


@app.route("/", methods=['GET'])
def index():
    return Response("Enhorabuena, has encontrado la pagina principal del microservicio de gestion de estaciones.", status = 200)

@app.route("/aniadir_estacion/<int:id>/<dir>/<int:n_puestos>", methods=['PUT'])
def aniadir_estacion(id, dir, n_puestos):
    result = estaciones.aniadir_estacion(id, dir, n_puestos)
    if result == "Estacion añadida":
        return Response("Estacion añadida", status = 200)
    else:
        print(result)
        return Response("Datos no validos", status = 400)

@app.route("/estacion/<int:id>", methods=['GET'])
def get_estacion(id):
    estac = estaciones.get_estacion_by_id(id)
    if estac != None:
        estac_dict = estacion_to_dict(estac)
        return Response(json.dumps(estac_dict), status=200, mimetype="application/json")
    else:
        return "No hay ninguna estacion con ese ID"

@app.route("/all_estaciones", methods=['GET'])
def get_all_estaciones():
    result = []
    for estacion in estaciones.estaciones:
        estac = {}
        estac = estacion_to_dict(estacion)
        result.append(estac)
    if result == []:
        return Response("No hay ninguna estacion",status=204)
    else:
        return Response(json.dumps(result), status=200, mimetype="application/json")

@app.route("/borrar_estacion/<int:id>", methods=['GET'])
def borrar_estacion(id):
    result = estaciones.eliminar_estacion(id)
    if result == "Esa estacion no existe, no se hace nada":
        return Response("Esa estacion no existe", status=400)
    else:
        return Response("Eliminada", status=200)
