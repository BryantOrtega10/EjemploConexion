from app.datos.MysqlConnector import MysqlConnection


class ItemCarritoAdicionModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_itemCarrito, id_producto, id_adicion, cantidad, precio):
        res = self.__conector.insert("item_carrito_adicion", {"fk_item_carrito": id_itemCarrito,
                                                              "fk_producto": id_producto,
                                                              'fk_adicion': id_adicion,
                                                              'cantidad': cantidad,
                                                              'precio': precio})
        if res['success'] == True:
            self.__conector.commit()

        return res

    # Trae la informacion de las adiciones relacionadas con un producto y un item de carrito
    def obtenerInfoAdiciones(self, id_itemCarrito):
        if id_itemCarrito != '':
            res = self.__conector.select(fields=["fk_producto", 'fk_adicion', 'cantidad', 'precio'],
                                         tables=["item_carrito_adicion"],
                                         where="fk_item_carrito=%(id_itemCarrito)s",
                                         values={"id_itemCarrito": id_itemCarrito})
            return res
