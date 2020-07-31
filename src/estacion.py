# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán

"""
from bikebd import BikeBD
from bicicleta import Bicicleta
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
                result = True
        return result

    def get_puestosLibres(self):
        return self.__nPuestos

    def depositar_bicicleta(self, bicicleta):
        mensaje = ""
        if self.puestos_libres > 0:
            if self.check_bici_almacenada(bicicleta):
                mensaje = "No se puede almacenar una bicicleta con el mismo id que otra"
            elif bicicleta.get_disponible() == False:
                self.bicis.append(bicicleta)
                Bicicletas.get_bici_by_id(bicicleta.ID).set_disponible(True)
                self.puestos_libres -=1
                mensaje = "Bicicleta depositada con exito"
            else:
                mensaje = "La bicicleta parece estar almacenada en alguna otra estacion :/ "
        else:
            mensaje = "No cogen mas bicicletas en esta estación"
        return mensaje


    def retirar_bicicleta(self, bicicleta, usuario):
        mensaje = ""
        if self.check_bici_almacenada(bicicleta) == False:
            mensaje = "La bicicleta no se encuentra en esta estación"
        elif usuario == None or usuario == "" or not isinstance(usuario, str):
            mensaje = "Usuario no valido"
        elif bicicleta.get_disponible() == True:
            self.bicis.remove(bicicleta)
            self.puestos_libres += 1
            bicicleta.disponible = False
            bicicleta.add_ultimo_usuario(usuario)
            mensaje = "Bicicleta retirada con exito"
        return mensaje

Bicis_BD = BikeBD()
Bicis_BD.aniadir_bici(1,22)
Bicis_BD.add_ultimo_usuario(1, "Fernando")

Estacion_BD = StationBD()
Estacion_BD.aniadir_estacion(1, "calle tal", 2)
bici = Bicis_BD.get_bici_by_id(1)
Estacion_BD.depositar_bicicleta(1, 1)
Estacion_BD.retirar_bicicleta(1)
estacion.retirar_bicicleta(bici, "Fernando")
