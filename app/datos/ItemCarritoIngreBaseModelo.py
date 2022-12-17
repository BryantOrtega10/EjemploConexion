from app.datos.MysqlConnector import MysqlConnection


class ItemCarritoIngredienteBaseModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_itemCarrito, id_producto, id_ingediente_base, cantidad):
        res = self.__conector.insert("item_carrito_ingrediente_base", {"fk_item_carrito": id_itemCarrito,
                                                                       "fk_producto": id_producto,
                                                                       'fk_ingediente_base': id_ingediente_base,
                                                                       'cantidad': cantidad})
        if res['success'] == True:
            self.__conector.commit()

        return res

    # Trae la informacion de los ingredientes base relacionados con un producto y un item de carrito
    def obtenerInfoIngredientesBase(self, id_itemCarrito):
        if id_itemCarrito != '':
            res = self.__conector.select(fields=["fk_producto", 'fk_ingrediente_base', 'cantidad'],
                                         tables=["item_carrito_ingrediente_base"],
                                         where="fk_item_carrito=%(id_itemCarrito)s",
                                         values={"id_itemCarrito": id_itemCarrito})
            return res
