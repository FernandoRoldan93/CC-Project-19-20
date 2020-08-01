# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán

"""
from bicicletas import Bicicletas
from estacion import Estacion
class StationBD:

    def __init__(self):
        self.estaciones = []

    def aniadir_estacion(self, nueva_estacion):
        if datos_correctos(nueva_estacion) and self.valid_ID(nueva_estacion.id): self.estaciones.append(estacion)
        return

    def valid_ID(self, ID):
        valid = True
        for estacion in self.estaciones:
            if estacion.ID == ID:
                valid = False

        return valid

    def check_data_types(self, estacion):
        valid = False
        if isinstance(estacion.ID, str) and isinstance(estacion.direccion, str) and isinstance(estacion.nPuestos, str)
            and isinstance(estacion.puestos_libres, str) and isinstance(estacion.bicis, list):
                valid = true

        return valid

    def datos_correctos(self, datos_estacion):
        valid = False

        if self.valid_ID(datos_estacion.ID):
            if check_data_types(datos_estacion):
                valid = True

        return valid

    def get_estacion_by_id(self, id):
        result = None
        for estacion in estaciones:
            if id == estacion.ID:
                result = estacion

        return result


    """comprueba si una bici esta almacenada en esta estacion"""
    def check_bici_almacenada(self, estacion_id, bicicleta_id):
        estacion = get_estacion_by_id()

        return any(bici.ID == bicicleta_id for bici in estacion.bicis)


    def depositar_bicicleta(self, estacion_id, bicicleta_id):
        mensaje = ""
        station = get_estacion_by_id(estacion_id)

        if station.puestos_libres > 0:
            if check_bici_almacenada(estacion_id, bicicleta_id) == True:
                mensaje = "Ya hay una bicicleta con ese ID almacenada"
            else:
                station.bicis.append(bicicleta)
                bicicleta.set_ocupada(False)
                self.puestos_libres -=1
                mensaje = "Bicicleta depositada con exito"
        else:
            mensaje = "No cogen mas bicicletas en esta estación"

        return mensaje

    def retirar_bicicleta(self, bicicleta, usuario):
        mensaje = ""
        if self.check_bici_almacenada(bicicleta) == False:
            mensaje = "La bicicleta no se encuentra en esta estación"
        elif usuario == None or usuario == "":
            mensaje = "Usuario no valido"
        else:
            self.bicicletas_estacionadas[bicicleta.id] = bicicleta
            self.puestos_libres += 1
            bicicleta.set_ocupada(True)
            bicicleta.add_ultimo_usuario(usuario)
            mensaje = "Bicicleta retirada con exito"

        return mensaje

    def get_puestosLibres(self):
        return self.nPuestos
