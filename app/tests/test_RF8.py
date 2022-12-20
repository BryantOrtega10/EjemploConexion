import pytest

from app.objetos_sesion.Carrito import Carrito

# Obtiene el menu configurado y guardado por el cliente
@pytest.fixture
def menu():
    carritoPrueba = Carrito()
    carritoPrueba.setBdInfoCarrito(1)
    itemCarrito = carritoPrueba.getItemsCarrito()[0]
    menu = itemCarrito.getMenu()
    return menu

# Test que compreuba la correcta funcionalidad del sistema para cargar en sesion los menus de los clientes
def test_obtener_menu_cliente(menu):
    id_menu = menu.getIdMenu()
    assert id_menu == 1011