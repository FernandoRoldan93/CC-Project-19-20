# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán

"""
import sys
sys.path.append('src/')

from bikebd import BikeBD
from bicicleta import Bicicleta
from stationbd import StationBD
from estacion import Estacion

""" Test 1: Comprobar si se puede añadir una bicicleta """
def test_aniadir_estacion():
    estaciones = StationBD()
    assert estaciones.aniadir_estacion(1, "Gonzalo Gallas", 1) == "Estacion añadida"


""" Test 2: Tras retirar una bicicleta, esta queda ocupada"""
def test_bici_ocupada():
    estaciones = StationBD()
    estaciones.aniadir_estacion(1, "Gonzalo Gallas", 1)
    estac = estaciones.get_estacion_by_id(1)
    print(estac)
    bici = Bicicleta(1,2010)
    estaciones.depositar_bicicleta(estac, bici)
    estaciones.retirar_bicicleta(estac, bici, "Fernando")
    assert bici.disponible == False


""" Test 3: Para depositar una bicicleta en una estacion ha de haber huecos libres"""
def test_depositar_bici():
    bici = Bicicleta(1, 2010)
    bici1 = Bicicleta(2, 2010)
    estaciones = StationBD()
    estaciones.aniadir_estacion(1, "Gonzalo Gallas", 1)
    estac = estaciones.get_estacion_by_id(1)
    estaciones.depositar_bicicleta(estac, bici)
    assert estaciones.depositar_bicicleta(estac,bici1) == "No cogen mas bicicletas en esta estación"

""" Test 4: No se puede sacar una bicicleta de una estación en la cual no esta esa bicicleta """
def test_sacar_bici():
    bici = Bicicleta(1,2010)
    usuario = "Fernando"
    estaciones = StationBD()
    estaciones.aniadir_estacion(1, "Gonzalo Gallas", 1)
    estaciones.aniadir_estacion(2, "Facultad Ciencias", 1)
    estac1 = estaciones.get_estacion_by_id(1)
    estac2 = estaciones.get_estacion_by_id(2)
    estaciones.depositar_bicicleta(estac1, bici)
    assert estaciones.retirar_bicicleta(estac1, bici, usuario) == "Bicicleta retirada con exito" \
    and estaciones.retirar_bicicleta(estac2, bici, usuario) == "La bicicleta no se encuentra en esta estación"


""" Test 5: Al retirar una bicicleta se ha de especificar un usuario no nulo """
def test_usuario_no_nulo():
    bici = Bicicleta(1,2010)
    usuario = 1
    estaciones = StationBD()
    estaciones.aniadir_estacion(1, "Gonzalo Gallas", 1)
    estac = estaciones.get_estacion_by_id(1)
    estaciones.depositar_bicicleta(estac, bici)
    assert estaciones.retirar_bicicleta(estac, bici, usuario) == "Usuario no valido"


""" Test 6: No se puede almacenar una misma bicicleta 2 veces en la misma estación """
def test_no_repetir_bicicleta():
    bici = Bicicleta(1,2010)
    estaciones = StationBD()
    estaciones.aniadir_estacion(1, "Gonzalo Gallas", 2)
    estac = estaciones.get_estacion_by_id(1)
    estaciones.depositar_bicicleta(estac, bici)
    assert estaciones.depositar_bicicleta(estac, bici) == "No se puede almacenar una bicicleta con el mismo id que otra"


""" Test 7: No se puede retirar una bicicleta de una estación en la que no esta """
def test_retirar_bicicleta_otra_estacion():
    bici = Bicicleta(1,2010)
    bici1 = Bicicleta(2, 2010)
    estaciones = StationBD()
    estaciones.aniadir_estacion(1, "Gonzalo Gallas", 2)
    estac = estaciones.get_estacion_by_id(1)
    estaciones.depositar_bicicleta(estac, bici)
    assert estaciones.retirar_bicicleta(estac, bici1, "Fernan") == "La bicicleta no se encuentra en esta estación"

""" Test 8: Tras retirar una bicicleta, el usuario queda registrado."""

def test_usuario_retira():
    bici = Bicicleta(1,2010)
    estaciones = StationBD()
    estaciones.aniadir_estacion(1, "Gonzalo Gallas", 2)
    estac = estaciones.get_estacion_by_id(1)
    estaciones.depositar_bicicleta(estac, bici)
    usuario = "Fernando"
    estaciones.retirar_bicicleta(estac, bici, usuario)
    usuarios = bici.get_ultimos_usuarios()
    assert usuarios[-1] == "Fernando"

""" Test 9: Al eliminar una estacion esta ya no se puede consultar """
def test_eliminar_estacion():
    estaciones = StationBD()
    estaciones.aniadir_estacion(1, "Gonzalo Gallas", 1)
    assert estaciones.eliminar_estacion(1) == "Eliminada"

""" Test 10: No se puede eliminar una estacion que no existe """
def test_intentar_eliminar_estacion():
    estaciones = StationBD()
    assert estaciones.eliminar_estacion(1) == "Esa estacion no existe, no se hace nada"
