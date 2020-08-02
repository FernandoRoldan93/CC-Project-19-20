# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán
"""

class Bicicleta:
    def __init__(self, id, fecha_alta):
            self.id = id
            self.fecha_alta = fecha_alta
            self.disponible = True
            self.__ultimos_usuarios = []

    def set_disponible(self, disponible):
        if self.disponible == disponible:
            return "Esta bicicleta ya se encuentra en el estado que quieres asignar "
        else:
            self.disponible = disponible
            return "Estado cambiado correctamente :D"

    def get_disponible(self):
        return self.disponible

    def add_ultimo_usuario(self, usuario):
        if usuario == "" or usuario == None:
            return "Se ha de especificar un usuario"
        else:
            self.__ultimos_usuarios.append(usuario)
            return "Añadido usuario al registro de la bicicleta"

    def get_ultimos_usuarios(self):
        return self.__ultimos_usuarios

    def __str__(self):
        output = f"id = {self.id} ; fecha_alta = {self.fecha_alta} ; Disponible = {self.disponible};"
         + f"ultimos_usuarios = {self.__ultimos_usuarios}"

        return output
