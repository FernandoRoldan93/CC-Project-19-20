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

""" Test 3: Para depositar una bicicleta en una estacion ha de haber huecos libres"""
def test_bici_id():
    bicis_bd = BikeBD()
    bicis_bd.aniadir_bici(1, 2020)
    bici1 = bicis_bd.get_bici_by_id(1)
    bici1_index= bicis_bd.get_bici_index(1)
    assert bici1 is bicis_bd.bicicletas[bici1_index]

""" Test 4: Al retirar una bicicleta se ha de especificar un usuario no nulo """
def test_usuario_no_valido():
    bicis_bd = BikeBD()
    bicis_bd.aniadir_bici(1, 2020)
    bicis_bd.add_ultimo_usuario(1, "")
    error = "Se ha de especificar un usuario valido"
    assert bicis_bd.add_ultimo_usuario(1, "") == error and bicis_bd.add_ultimo_usuario(1, None) == error

""" Test 5:Los usuarios se almacenan correctamente en la lista de ultimos usuarios de las bicicletas"""
def test_guarda_usuario():
    bicis_bd = BikeBD()
    bicis_bd.aniadir_bici(1, 2020)
    result = bicis_bd.add_ultimo_usuario(1, "Fernando")
    assert "Fernando" in bicis_bd.get_ultimos_usuarios(1)
