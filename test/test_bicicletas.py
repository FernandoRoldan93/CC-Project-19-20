# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán

"""
import sys
sys.path.append('src/')

from bicicletas import Bicicleta
from estacion import Estacion


""" Test 1: Tras retirar una bicicleta, esta queda ocupada"""
def test_bici_ocupada():
    bici = Bicicleta(1,2010)
    estac = Estacion(1, "Gonzalo Gallas", 1)
    estac.depositar_bicicleta(bici)
    estac.retirar_bicicleta(bici, "Fernando")
    assert bici.get_ocupada() == True
    

""" Test 2: Para depositar una bicicleta en una estacion ha de haber huecos libres"""
def test_depositar_bici():
    bici = Bicicleta(1, 2010)
    bici1 = Bicicleta(2, 2010)
    estac = Estacion(1, "Gonzalo Gallas", 1)
    estac.depositar_bicicleta(bici)
    assert estac.depositar_bicicleta(bici1) == "No cogen mas bicicletas en esta estación"

""" Test 3: No se puede sacar una bicicleta de una estación en la cual no esta esa bicicleta """
def test_sacar_bici():
    bici = Bicicleta(1,2010)
    usuario = "Fernando"
    estac = Estacion(1, "Gonzalo Gallas", 1)
    assert estac.retirar_bicicleta(bici, usuario) == "La bicicleta no se encuentra en esta estación"


""" Test 4: Al retirar una bicicleta se ha de especificar un usuario no nulo """
def test_usuario_no_nulo():
    bici = Bicicleta(1,2010)
    estac = Estacion(1, "Gonzalo Gallas", 1)
    estac.depositar_bicicleta(bici)
    assert estac.retirar_bicicleta(bici, None) == "Usuario no valido"


""" Test 5: No se puede almacenar una misma bicicleta 2 veces en la misma estación """
def test_no_repetir_bicicleta():
    bici = Bicicleta(1,2010)
    estac = Estacion(1, "Gonzalo Gallas", 2)
    estac.depositar_bicicleta(bici)
    assert estac.depositar_bicicleta(bici) == "No se puede almacenar una bicicleta con el mismo id que otra"


""" Test 6: No se puede retirar una bicicleta de una estación en la que no esta """
def test_retirar_bicicleta_otra_estacion():
    bici = Bicicleta(1,2010)
    bici1 = Bicicleta(2, 2010)
    estac = Estacion(1, "Gonzalo Gallas", 2)
    estac.depositar_bicicleta(bici)
    assert estac.retirar_bicicleta(bici1, "asd") == "La bicicleta no se encuentra en esta estación"
    