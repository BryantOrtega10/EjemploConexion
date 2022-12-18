from app.logica.MenuControlador import MenuControlador
from app.logica.ProductoControlador import ProductoControlador
from app.objetos_sesion.Adicion import Adicion
from app.objetos_sesion.PlatoFuerte import PlatoFuerte
from app.objetos_sesion.Bebida import Bebida
from app.objetos_sesion.Menu import Menu
from app.objetos_sesion.ItemCarrito import ItemCarrito
from app.objetos_sesion.Carrito import Carrito


# adicion1 = Adicion()
# adicion2 = Adicion()
# platoFuerte1 = PlatoFuerte()
# platoFuerte2 = PlatoFuerte()
# platoFuerte3 = PlatoFuerte()
# platoFuerte4 = PlatoFuerte()
# platoFuerte5 = PlatoFuerte()
# bebida1 = Bebida()
# menu1 = Menu()
# menu2 = Menu()
#
# adicion1.setBdInfoAdicion(101)
# adicion2.setBdInfoAdicion(213)
# platoFuerte1.setBdInfoProducto(101)
# platoFuerte2.getBdInfoProducto(101)
# platoFuerte3.getBdInfoProducto(1003)
# platoFuerte4.getBdInfoProducto(101)
# platoFuerte5.getBdInfoProducto(1003)
# bebida1.setBdInfoProducto(102)
# menu1.setBdInfoMenu(101)
# menu2.setBdInfoMenu(1011)
#
# # productos modificados por el cliente
# platoFuerte1.setAdiciones([adicion1, adicion2])
# platoFuerte1.setAdicionesSeleccionadas([adicion1, adicion1])
#
# platoFuerte2.setAdiciones([adicion1, adicion2])
# platoFuerte2.setAdicionesSeleccionadas([adicion1, adicion2])
#
# platoFuerte3.setAdiciones([adicion2])
# platoFuerte3.setAdicionesSeleccionadas([adicion2, adicion2, adicion2])
#
# # producto base de menu
# platoFuerte4.setAdiciones([adicion1, adicion2])
# platoFuerte5.setAdiciones([adicion2])
#
# # menus
# menu1.setEstado("En memoria")
# menu1.setBebida(bebida1)
# menu1.setPlatoFuerte(platoFuerte4)
#
# menu2.setEstado("En memoria")
# menu2.setPlatoFuerte(platoFuerte5)

# adicion1 = Adicion(101, "ALBONDIGA", "albondiga.jpg", "unidad", 101, 1, 10, 5000)
# adicion2 = Adicion(13, "tocineta", "workinprogress", "gramos", 213, 1, 10, 9900)

#producto_modificados_por_cliente
# platoFuerte1 = PlatoFuerte(101, "PASTA BOLOÑESA", 20000, "pastaBoloniesa.jpg", [], [], [adicion1, adicion2], [adicion1, adicion1], 0, False, 0, False)
# platoFuerte2 = PlatoFuerte(101, "PASTA BOLOÑESA", 20000, "pastaBoloniesa.jpg", [], [], [adicion1, adicion2], [adicion1, adicion2], 0, False, 0, False)
# platoFuerte3 = PlatoFuerte(1003, "HAMBURGUESA MCNIFICA", 28000, "mcnifica.jpg", [], [], [adicion2], [adicion2,adicion2,adicion2], 0, False, 0, False)
# #producto base de menu
# platoFuerte4 = PlatoFuerte(101, "PASTA BOLOÑESA", 20000, "pastaBoloniesa.jpg", [], [], [adicion1, adicion2], [], 0, False, 0, False)
# platoFuerte5 = PlatoFuerte(1003, "HAMBURGUESA MCNIFICA", 28000, "mcnifica.jpg", [], [], [adicion2], [], 0, False, 0, False)
# bebida1 = Bebida(102, "GASEOSA MANZANA 200 ML", 2500, "gaseosaManzana200.jpg", [], [], [], [], 0, False, 0, False)
#
#
# menu1 = Menu(101, "COMBO PASTA BOLOÑESA", "comboPastaBoloniesa.png", 22000, "En memoria", None, bebida1, None, platoFuerte4, None)
# menu2 = Menu(1011, "COMBO MCCOMBO", "combomccombo.png", 25000, "En memoria", None, None, None, platoFuerte5, None)
#
# itemCarrito1 = ItemCarrito(1, menu1, "sede1", [bebida1, platoFuerte2])
# itemCarrito2 = ItemCarrito(2, menu2, "sede2", [platoFuerte5])
# itemCarrito3 = ItemCarrito(3, menu2, "sede2", [bebida1, platoFuerte3])
#
# carrito = Carrito(1, 0, [itemCarrito1, itemCarrito2, itemCarrito3], "cliente", None, "En memoria")
# print(carrito.calcularValor())

# pruebas aparte
from app.datos.ProductoIngreBaseModelo import ProductoIngredienteBaseModelo
from app.logica.ProductoControlador import ProductoControlador

ingredientes_base = [
    {
        'id_ingrediente_base': 101,
        'auto_select': 1,
        'cantidad': 500,
        'id_ingrediente': 100
    },
    {
        'id_ingrediente_base': 102,
        'auto_select': 1,
        'cantidad': 3,
        'id_ingrediente': 101
    },
    {
        'id_ingrediente_base': 103,
        'auto_select': 1,
        'cantidad': 20,
        'id_ingrediente': 102
    }
]
adiciones = [
    {
        'id_adicion': 101,
        'precio': 5000
    },
    {
        'id_adicion': 213,
        'precio': 9900
    }
]
request = {
    'nombre': 'PASTA BOLOÑESA',
    'precio': 20000,
    'tipo': 1,
    'foto': 'pastaBoloniesa.jpg',
    'maximo_ingredientes_base': 0,
    'aplica_maximo': 0,
    'minimo_ingredientes_base': 0,
    'aplica_minimo': 0,
    'id_restaurante': 3,
    'adiciones': adiciones,
    'ingredientes_base': ingredientes_base,

}

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
menuPrueba = MenuControlador()
# print(menuPrueba.tempAgregar(requestMenu))
print(menuPrueba.eliminar(1012))