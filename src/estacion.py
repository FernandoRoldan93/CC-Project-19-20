# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán

"""
from bicicletas import Bicicleta
class Estacion:
    def __init__(self, id, direccion, nPuestos):
            self.__id = id
            self.direccion = direccion
            self.__nPuestos = nPuestos
            self.puestos_libres = self.__nPuestos
            self.bicicletas_estacionadas = {}
        
    def datos_correctos(self):
        if self.id == None or self.direccion == None or self.__nPuestos <= 0 or self.__nPuestos == None:
            return False
        else:
            return True

    def get_id(self):
        return self.__id
    
    """comprueba si una bici esta almacenada en esta estacion"""
    def check_bicis_almacenada(self, bicicleta):
        return bicicleta.id in self.bicicletas_estacionadas.keys()
    
    def depositar_bicicleta(self, bicicleta):
        mensaje = ""
        if self.puestos_libres > 0:
            if self.check_bicis_almacenada(bicicleta) == True:
                mensaje = "No se puede almacenar una bicicleta con el mismo id que otra"
            else:
                self.bicicletas_estacionadas[bicicleta.id] = bicicleta
                bicicleta.set_ocupada(False)
                self.puestos_libres -=1
                mensaje = "Bicicleta depositada con exito"                 
        else:
            mensaje = "No cogen mas bicicletas en esta estación"
        
        return mensaje
        
    def retirar_bicicleta(self, bicicleta, usuario):
        mensaje = ""
        if self.check_bicis_almacenada(bicicleta) == False:
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
        return self.__nPuestos
        