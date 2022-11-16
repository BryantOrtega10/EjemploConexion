from app.objetos_sesion.Adicion import Adicion
from app.objetos_sesion.PlatoFuerte import PlatoFuerte
from app.objetos_sesion.Bebida import Bebida
from app.objetos_sesion.Menu import Menu
from app.objetos_sesion.ItemCarrito import ItemCarrito
from app.objetos_sesion.Carrito import Carrito


adicion1 = Adicion(101, "ALBONDIGA", "albondiga.jpg", "unidad", 101, 1, 10, 5000)
adicion2 = Adicion(13, "tocineta", "workinprogress", "gramos", 213, 1, 10, 9900)

#producto_modificados_por_cliente
platoFuerte1 = PlatoFuerte(101, "PASTA BOLOÑESA", 20000, "pastaBoloniesa.jpg", [], [], [adicion1, adicion2], [adicion1, adicion1], 0, False, 0, False)
platoFuerte2 = PlatoFuerte(101, "PASTA BOLOÑESA", 20000, "pastaBoloniesa.jpg", [], [], [adicion1, adicion2], [adicion1, adicion2], 0, False, 0, False)
platoFuerte3 = PlatoFuerte(1003, "HAMBURGUESA MCNIFICA", 28000, "mcnifica.jpg", [], [], [adicion2], [adicion2,adicion2,adicion2], 0, False, 0, False)
#producto base de menu
platoFuerte4 = PlatoFuerte(101, "PASTA BOLOÑESA", 20000, "pastaBoloniesa.jpg", [], [], [adicion1, adicion2], [], 0, False, 0, False)
platoFuerte5 = PlatoFuerte(1003, "HAMBURGUESA MCNIFICA", 28000, "mcnifica.jpg", [], [], [adicion2], [], 0, False, 0, False)
bebida1 = Bebida(102, "GASEOSA MANZANA 200 ML", 2500, "gaseosaManzana200.jpg", [], [], [], [], 0, False, 0, False)


menu1 = Menu(101, "COMBO PASTA BOLOÑESA", "comboPastaBoloniesa.png", 22000, "En memoria", None, bebida1, None, platoFuerte4, None)
menu2 = Menu(1011, "COMBO MCCOMBO", "combomccombo.png", 25000, "En memoria", None, None, None, platoFuerte5, None)


itemCarrito1 = ItemCarrito(1, menu1, "sede1", [bebida1, platoFuerte2])
itemCarrito2 = ItemCarrito(2, menu2, "sede2", [platoFuerte5])
itemCarrito3 = ItemCarrito(3, menu2, "sede2", [bebida1, platoFuerte3])

carrito = Carrito(1,0, [itemCarrito1, itemCarrito2, itemCarrito3], "cliente", None, "En memoria")
print(carrito.calcularValor())


