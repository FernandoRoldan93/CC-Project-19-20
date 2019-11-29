# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán  
"""

class Bicicleta:
    def __init__(self, id, fecha_alta, ultimos_usuarios):
        if id == None or id == "" or fecha_alta == None or fecha_alta == "":
            return "Datos no validos"
        else:
            self.id = id
            self.fecha_alta = fecha_alta
            self.__disponible = True
            self.__ocupada = False
            self.__ultimos_usuarios = [None]

    def set_ocupada(self, ocupada):
        if self.__ocupada == ocupada:
            return "Esta bicicleta ya se encuentra en el estado que quieres asignar "
        else:
            self.__ocupada = ocupada
            return "Estado cambiado correctamente :D"

    def get_ocupada(self):
        return self.__ocupada

    def add_ultimo_usuario(self, usuario):
        if usuario == "" or usuario == None:
            return "Se ha de especificar un usuario"
        else:
            self.__ultimos_usuarios.append()
            return "Añadido usuario al registro de la bicicleta"
    
    def get_ultimos_usuarios(self):
        return self.__ultimos_usuarios

    def set_disponible(self, disponible):
        if self.__disponible == True:
            return "Esta bicicleta ya se encuentra en el estado que quieres asignar "
        else:
            self.__disponible = True
            return "Estado cambiado correctamente :D"

    def get_disponible(self):
        return self.__disponible