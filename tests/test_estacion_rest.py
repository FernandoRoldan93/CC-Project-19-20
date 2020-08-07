# -*- coding: utf-8 -*-
"""
@author: Fernando Roldán

"""
import sys
sys.path.append('src/')
import estacion_rest

app = estacion_rest.app.test_client()

""" Test 1: Comprueba que haya conexion a la api """
def test_conexion():
    result = app.get('/')
    assert (result.status_code == 200)

""" Test 2: Si no hay ninguna estacion, se devuelve un archivo vacio """
def test_no_data():
    result = app.get('/all_estaciones')
    assert result.status_code == 204

""" Test 2: Los datos de prueba se añaden al llamar al metodo correspondiente """
def test_dummy_data():
    app.get('/test_data')
    result = app.get('/all_estaciones')
    assert result.status_code == 200

""" Test 3: Tras añadir datos, la respuesta es correcta """
def test_aniadir():
    result = app.put('/aniadir_estacion/3/Ciencias/20')
    assert result.status_code == 200

""" Test 4: No se puede añadir dos veces la misma estacion """
def test_estacion_repetida():
    app.put('/aniadir_estacion/1/Ciencias/20')
    result = app.put('/aniadir_estacion/1/Ciencias/20')
    assert result.status_code == 400

""" Test 5: Se puede eliminar una estacion existente """
def eliminar_estacion():
    result = app.put('/borrar_estacion/1')
    assert result.status_code == 200

""" Test 6: No se puede eliminar una estacion que no existe """
def eliminar_estacion():
    result = app.put('/borrar_estacion/5')
    assert result.status_code == 400
