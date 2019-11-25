# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

class Bicicleta:
    def __init__(self, id, fecha_alta, ultimos_usuarios):
        self.id = id
        self.fecha_alta = fecha_alta
        self.__ocupada = False
        self.__ultimos_usuarios = [None]
    
