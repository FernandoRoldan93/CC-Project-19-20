# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán

"""
import sys
sys.path.append('../src/')

from bicicletas import Bicicleta
from estacion import Estacion
    


    bici = Bicicleta.bicicletas(None, 2010)
    estac = Estacion(1, "Gonzalo Gallas", 2)
""" Test 1: Al crear una bicicleta ningun campo puede ser nulo"""
def test_añadir_bicicleta_no_nulo():
    assert Bicicleta(None, 2010) == "Datos no validos"
    
    
""" Test 2: Al crear una estación ningun campo puede ser nulo"""
def test_añadir_estacion_no_nulo():
    assert Estacion(1, "Gonzalo Gallas", 0) == "Datos no validos"


""" Test 3: Para depositar una bicicleta en una estacion ha de haber huecos libres"""
def test_depositar_bici():
    bici = Bicicleta(1, 2010)
    bici = Bicicleta(2, 2010)
    estac = estacion.Estacion(1, "Gonzalo Gallas", 1)
    estac.depositar_bicicleta(bici)
    assert estac.depositar_bicicleta(bici1) == "No cogen mas bicicletas en esta estación"

""" Test 4: No se puede sacar una bicicleta de una estación en la cual no esta esa bicicleta """
def test_sacar_bici():
    bici = Bicicleta(1,2010)
    usuario = "Fernando"
    estac = estacion.Estacion(1, "Gonzalo Gallas", 1)
    assert estac.retirar_bicicleta(bici, usuario) == "La bicicleta no se encuentra en esta estación"


""" Test 5: Al retirar una bicicleta se ha de especificar un usuario no nulo """
    bici = bicicletas.Bicicleta(1,2010)
    estac = estacion.Estacion(1, "Gonzalo Gallas", 1)
    assert estac.retirar_bicicleta(bici, None) == "Usuario no valido"


""" Test 6: No se puede almacenar una misma bicicleta 2 veces en la misma estación """

""" Test 7: No se puede retirar una bicicleta de una estación en la que no esta """
