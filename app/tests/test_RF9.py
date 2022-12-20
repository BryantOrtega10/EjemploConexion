import pytest

from app.objetos_sesion.Adicion import Adicion
from app.objetos_sesion.Bebida import Bebida
from app.objetos_sesion.Carrito import Carrito
from app.objetos_sesion.ItemCarrito import ItemCarrito
from app.objetos_sesion.Menu import Menu
from app.objetos_sesion.PlatoFuerte import PlatoFuerte

# Ingredientes artificiales para el test
@pytest.fixture
def ingredientes():
    ingredientes = {
        "adicion1": Adicion(101, "ALBONDIGA", "albondiga.jpg", "unidad", 101, 1, 10, 5000),
        "adicion2": Adicion(13, "tocineta", "workinprogress", "gramos", 213, 1, 10, 9900)
    }
    return ingredientes

# productos artificiales para el test
@pytest.fixture
def productos(ingredientes):
    adicion1 = ingredientes['adicion1']
    adicion2 = ingredientes['adicion2']
    # Del 1-3 son platos "modificados por el cliente", el 4 y 5 son platos base del menu
    platosFuertes = {
        "platoFuerte1": PlatoFuerte(101, "PASTA BOLOÑESA", 20000, "pastaBoloniesa.jpg", [], [], [adicion1, adicion2],
                                    [adicion1, adicion1], 0, False, 0, False),
        "platoFuerte2": PlatoFuerte(101, "PASTA BOLOÑESA", 20000, "pastaBoloniesa.jpg", [], [], [adicion1, adicion2],
                                    [adicion1, adicion2], 0, False, 0, False),
        "platoFuerte3": PlatoFuerte(1003, "HAMBURGUESA MCNIFICA", 28000, "mcnifica.jpg", [], [], [adicion2],
                                    [adicion2, adicion2, adicion2], 0, False, 0, False),
        "platoFuerte4": PlatoFuerte(101, "PASTA BOLOÑESA", 20000, "pastaBoloniesa.jpg", [], [], [adicion1, adicion2],
                                    [], 0, False, 0, False),
        "platoFuerte5": PlatoFuerte(1003, "HAMBURGUESA MCNIFICA", 28000, "mcnifica.jpg", [], [], [adicion2], [], 0,
                                    False, 0, False)
    }

    bebidas = {
        "bebida1": Bebida(102, "GASEOSA MANZANA 200 ML", 2500, "gaseosaManzana200.jpg", [], [], [], [], 0, False, 0,
                          False)
    }

    productos = {
        "platosFuertes": platosFuertes,
        "bebidas": bebidas
    }

    return productos

# menus artificiales para el test
@pytest.fixture
def menus(productos):
    menus = {
        "menu1": Menu(101, "COMBO PASTA BOLOÑESA", "comboPastaBoloniesa.png", 22000, "En memoria", None,
                      productos['bebidas']['bebida1'], None, productos['platosFuertes']['platoFuerte4'], None),
        "menu2": Menu(1011, "COMBO MCCOMBO", "combomccombo.png", 25000, "En memoria", None, None, None,
                      productos['platosFuertes']['platoFuerte5'], None)
    }
    return menus

# items de carrito artificiales para el test
@pytest.fixture
def itemsCarrito(menus, productos):
    itemsCarrito = {
        "itemCarrito1": ItemCarrito(1, menus["menu1"], "sede1",
                                    [productos['bebidas']['bebida1'], productos['platosFuertes']['platoFuerte2']]),
        "itemCarrito2": ItemCarrito(2, menus["menu2"], "sede2", [productos['platosFuertes']['platoFuerte5']]),
        "itemCarrito3": ItemCarrito(3, menus["menu2"], "sede2",
                                    [productos['bebidas']['bebida1'], productos['platosFuertes']['platoFuerte3']])
    }

    return itemsCarrito

# carrito artificial para el test
@pytest.fixture
def carritos(itemsCarrito):
    carritos = {
        "carrito1": Carrito(1, 0,
                            [itemsCarrito["itemCarrito1"], itemsCarrito["itemCarrito2"], itemsCarrito["itemCarrito3"]],
                            "cliente", None, "En memoria")
    }

    return carritos

# Test que comprueba el funcionamiento del calculo del valor de los carritos de compras
def test_carrito_calcular_valor(carritos):
    carrito = carritos["carrito1"]
    assert carrito.calcularValor() == 122100