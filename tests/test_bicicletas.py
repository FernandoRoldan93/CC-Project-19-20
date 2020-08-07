# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán

"""
import sys
sys.path.append('src/')

from bikebd import BikeBD
from bicicleta import Bicicleta

""" Test 1: Tras añadir una bici esta queda registrada"""
def test_existe_bici():
    bicis_bd = BikeBD()
    bicis_bd.aniadir_bici(1, 2020)
    assert bicis_bd.exists_id(1) == True

""" Test 2: No se puede añadir dos veces la misma bicicleta"""
def test_bici_repetida():
    bicis_bd = BikeBD()
    result = bicis_bd.aniadir_bici(1, 2020)
    result1 = bicis_bd.aniadir_bici(1, 2019)
    assert result == "Bici añadida con exito :D" and \
    result1 == "Ya existe una bici con ese ID, no se puede añadir :("

""" Test 3: No se puede especificar un usuario no valido """
def test_usuario_no_valido():
    bicis_bd = BikeBD()
    bicis_bd.aniadir_bici(1, 2020)
    bicis_bd.add_ultimo_usuario(1, "")
    error = "Se ha de especificar un usuario valido"
    assert bicis_bd.add_ultimo_usuario(1, "") == error and bicis_bd.add_ultimo_usuario(1, None) == error

""" Test 4:Los usuarios se almacenan correctamente en la lista de ultimos usuarios de las bicicletas"""
def test_guarda_usuario():
    bicis_bd = BikeBD()
    bicis_bd.aniadir_bici(1, 2020)
    result = bicis_bd.add_ultimo_usuario(1, "Fernando")
    assert "Fernando" in bicis_bd.get_ultimos_usuarios(1)
