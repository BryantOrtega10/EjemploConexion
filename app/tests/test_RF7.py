import pytest
from app.logica.MenuControlador import MenuControlador


# Menu que simula la seleccion de un cliente para la configuracion de su menu
@pytest.fixture
def menu():
    productos = [
        {'id_producto': 101},
        {'id_producto': 102}
    ]
    requestMenu = {
        'nombre': 'COMBO PASTA BOLOÑESA',
        'foto': 'comboPastaBoloniesa.png',
        'precio': 22000,
        'id_restaurante': 3,
        'productos': productos
    }
    return requestMenu


# Test que comprueba el funcionamiento del guardado de menus
def test_congig_menu(menu):
    menuControlador = MenuControlador()
    respuesta = menuControlador.tempAgregar(menu)
    assert respuesta['success'] == True
