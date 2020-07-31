# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán
"""
from bicicleta import Bicicleta

class Bicicletas:
    def __init__(self):
        self.bicicletas = []

    def get_ocupada(self):
        return self.__ocupada

    def get_bici_index(self, bicicleta_id):
        bici = self.get_bici_by_id(bicicleta_id)
        return bicicletas.index(bici)

    def exists_id(self, id):
        exists = False
        for bici in self.bicicletas:
            if bici.ID == id:
                exists = True
        return exists

    def aniadir_bici(self, id, fecha_alta):
        estado = ""
        if self.exists_id(id):
            estado = "Ya existe una bici con ese ID, no se puede añadir :("
        else:
            nueva_bici = Bicicleta(id, fecha_alta)
            self.bicicletas.append(nueva_bici)
            estado = "Bici añadida con exito :D"
        return estado

    def get_bici_by_id(self, id):
        result = None
        if exists_id(id):
            for bici in self.bicicletas:
                if bici.ID == id:
                    result = bici
        if result == None:
            return "No existe esa bicicleta"
        else:
            return result

    def add_ultimo_usuario(self, bici_id, usuario):
        if usuario == "" or usuario == None:
            return "Se ha de especificar un usuario"
        else:
            bici = get_bici_by_id(bici_id)
            bici.add_ultimo_usuario(usuario)
            return "Añadido usuario al registro de la bicicleta"

    def get_ultimos_usuarios(self, bici_id):
        bici = get_bici_by_id(bici_id)
        return bici.get_ultimos_usuarios()
