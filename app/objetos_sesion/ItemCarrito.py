from app.logica.ItemCarritoControlador import ItemCarritoControlador
from app.objetos_sesion.Menu import Menu
from app.objetos_sesion.Producto import Producto


class ItemCarrito:
    def __init__(self, idItemCarrito="", menu=None, sede=None, productos=[]):
        self.__idItemCarrito = idItemCarrito
        self.__menu = menu
        self.__sede = sede
        self.__productos = productos

        self.__itemCarritoControlador = ItemCarritoControlador()

    # Instancia toda la info del item carrito que hay en BD
    def setBdInfoItemCarrito(self, id_itemCarrito):
        infoItemCarrito = self.__itemCarritoControlador.obtener_x_id(id_itemCarrito)
        if infoItemCarrito:
            itemCarrito = infoItemCarrito['itemCarrito']
            self.__idItemCarrito = itemCarrito['id_item_carrito']
            for producto in infoItemCarrito['productos']:
                producto_obj = Producto()
                producto_obj.setBdInfoProducto(producto['fk_producto'])
                self.__productos.append(producto_obj)

            self.__menu = Menu()
            self.__menu.setBdInfoMenu(itemCarrito['fk_menu'])



    def getIdItemCarrito(self):
        return self.__idItemCarrito

    def setIdItemCarrito(self, value):
        self.__idItemCarrito = value

    def getMenu(self):
        return self.__menu

    def setMenu(self, value):
        self.__menu = value

    def getSede(self):
        return self.__sede

    def setSede(self, value):
        self.__sede = value

    def getProductos(self):
        return self.__productos

    def setProductos(self, value):
        self.__productos = value
