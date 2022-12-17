from app.datos.MysqlConnector import MysqlConnection


class ItemCarritoModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_carrito, id_menu, id_sede):
        if id_carrito == '':
            return {'success': False, 'error': "Id carrito vacio"}
        if id_menu == '':
            return {'success': False, 'error': "Id menu vacio"}
        if id_sede == '':
            return {'success': False, 'error': "Id sede vacio"}

        res = self.__conector.insert("item_carrito", {"fk_carrito": id_carrito, "fk_menu": id_menu, "fk_sede": id_sede})
        if res['success'] == True:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=["item_carrito"], limit=limite)
        return res

    def obtenerPorCarrito(self, id_carrito):
        res = self.__conector.select(fields=['id_item_carrito'], tables=['item_carrito'], where='fk_carrito=%(id_carrito)s', values={'id_carrito':id_carrito})
        return res

    def obtenerUno(self, id):
        res = self.__conector.select(tables=["item_carrito"], where=' id_item_carrito=%(id_item_carrito)s', values={"id_item_carrito":id})
        return res

    def modificar(self, id_item_carrito, id_carrito, id_menu, id_sede):
        if id_item_carrito == '':
            return {'success': False, 'error': "Id item carrito vacio"}
        if id_carrito == '':
            return {'success': False, 'error': "Id carrito vacio"}
        if id_menu == '':
            return {'success': False, 'error': "Id menu vacio"}
        if id_sede == '':
            return {'success': False, 'error': "Id sede vacio"}

        res = self.__conector.update("item_carrito",
                                     ["fk_carrito", "fk_menu", "fk_sede"],
                                     " id_item_carrito=%(id_item_carrito)s ",
                                     {"fk_carrito": id_carrito, "fk_menu": id_menu, "fk_sede": id_sede,
                                      "id_item_carrito": id_item_carrito})

        if res['success'] == True:
            self.__conector.commit()

        return res

    def eliminar(self, id_item_carrito):
        if id_item_carrito == '':
            return {'success': False, 'error': "Id item carrito vacio"}

        res = self.__conector.delete("item_carrito",
                                     " id_item_carrito=%(id_item_carrito)s ",
                                     {"id_item_carrito": id_item_carrito})

        if res['success'] == True:
            self.__conector.commit()

        return res
