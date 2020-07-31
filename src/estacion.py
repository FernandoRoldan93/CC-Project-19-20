# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán

"""
from bicicletas import Bicicletas
class Estacion:
    def __init__(self, id, direccion, nPuestos):
            self.id = id
            self.direccion = direccion
            self.nPuestos = nPuestos
            self.puestos_libres = self.nPuestos
            self.bicis = []

    """comprueba si una bici esta almacenada en esta estacion"""
    def check_bici_almacenada(self, bicicleta_id):
        result = False
            for bici in self.bicis:
                if bici.id == bicicleta_id:
                    result True

    def depositar_bicicleta(self, bicicleta_id):
        mensaje = ""
        bike = Bicicletas.get_bici_by_id(bicicleta_id)
        if self.puestos_libres > 0:
            if self.check_bici_almacenada(bicicleta_id):
                mensaje = "No se puede almacenar una bicicleta con el mismo id que otra"
            elif bike.get_disponible() == False:
                self.bicis.append(bicicleta)
                Bicicletas.get_bici_by_id(bicicleta_id).set_disponible(True)
                self.puestos_libres -=1
                mensaje = "Bicicleta depositada con exito"
            else:
                mensaje = "La bicicleta parece estar almacenada en alguna otra estacion :/ "

        else:
            mensaje = "No cogen mas bicicletas en esta estación"

        return mensaje

""" Por terminar
    def retirar_bicicleta(self, bicicleta_id, usuario):
        mensaje = ""
        bike = Bicicletas.get_bici_by_id(bicicleta_id)
        if self.check_bici_almacenada(bicicleta_id) == False:
            mensaje = "La bicicleta no se encuentra en esta estación"
        elif usuario == None or usuario == "":
            mensaje = "Usuario no valido"
        elif bike.get_disponible() == True:
            self.bicis.remove(bike)
            self.puestos_libres += 1

            bicicleta.set_ocupada(True)
            bicicleta.add_ultimo_usuario(usuario)
            mensaje = "Bicicleta retirada con exito"

        return mensaje
"""
    def get_puestosLibres(self):
        return self.__nPuestos
