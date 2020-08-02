# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán

"""
from bikebd import BikeBD
from estacion import Estacion
class StationBD:

    def __init__(self):
        self.estaciones = []

    def aniadir_estacion(self, id, direccion, nPuestos):
        nueva_estacion = Estacion(id, direccion, nPuestos)
        if self.datos_correctos(nueva_estacion):
            self.estaciones.append(nueva_estacion)
            return "Estacion añadida"
        else:
            return "Datos no validos"

    def valid_ID(self, ID):
        valid = True
        for estacion in self.estaciones:
            if estacion.id == ID:
                valid = False

        return valid

    def check_data_types(self, estacion):
        valid = False
        if isinstance(estacion.id, int) and isinstance(estacion.direccion, str) and isinstance(estacion.nPuestos, int):
                valid = True
        return valid

    def datos_correctos(self, datos_estacion):
        valid = False
        if self.valid_ID(datos_estacion.id) and self.check_data_types(datos_estacion):
            valid = True
        return valid

    def get_estacion_by_id(self, id):
        result = None
        for estacion in self.estaciones:
            if id == estacion.id:
                result = estacion

        return result


    """comprueba si una bici esta almacenada en esta estacion"""
    def check_bici_almacenada(self, estacion_id, bicicleta_id):
        estacion = self.get_estacion_by_id()

        return any(bici.id == bicicleta_id for bici in estacion.bicis)

    def depositar_bicicleta(self, estacion, bicicleta):
        mensaje = estacion.depositar_bicicleta(bicicleta)
        return mensaje

    def retirar_bicicleta(self, estacion, bicicleta, usuario):
        mensaje = estacion.retirar_bicicleta(bicicleta, usuario)
        return mensaje

    def get_puestosLibres(self):
        return self.nPuestos
