from app.datos.MysqlConnector import MysqlConnection


class ItemCarritoProductoModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_itemCarrito, id_producto):
        res = self.__conector.insert("item_carrito_producto", {"fk_item_carrito": id_itemCarrito,
                                                               "fk_producto": id_producto})
        if res['success'] == True:
            self.__conector.commit()

        return res

    def obtenerFKProductos(self, id_itemCarrito):
        if id_itemCarrito != '':
            res = self.__conector.select(fields=["fk_producto"],
                                         tables=["item_carrito_producto"],
                                         where="fk_item_carrito=%(id_itemCarrito)s",
                                         values={"id_itemCarrito": id_itemCarrito})
            return res
