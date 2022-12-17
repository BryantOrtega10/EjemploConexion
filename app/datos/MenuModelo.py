from app.datos.MysqlConnector import MysqlConnection


class MenuModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, nombre, foto, precio, id_restaurante):
        if nombre == '':
            return {'success': False, 'error': "Nombre vacio"}
        if foto == '':
            return {'success': False, 'error': "Foto vacia"}
        if precio == '':
            return {'success': False, 'error': "Precio vacio"}
        if id_restaurante == '':
            return {'success': False, 'error': "Id restaurante vacio"}

        res = self.__conector.insert("menu", {"nombre": nombre, "foto": foto, "precio": precio, "fk_restaurante": id_restaurante})
        if res['success'] == True:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=["menu"], limit=limite)
        return res

    def obtenerUno(self, id):
        res = self.__conector.select(tables=["menu"], where=' id_menu=%(id_menu)s', values={"id_menu":id})
        return res

    def modificar(self, id_menu, nombre, foto, precio, id_restaurante):
        if nombre == '':
            return {'success': False, 'error': "Nombre vacio"}
        if foto == '':
            return {'success': False, 'error': "Foto vacia"}
        if precio == '':
            return {'success': False, 'error': "Precio vacio"}
        if id_restaurante == '':
            return {'success': False, 'error': "Id restaurante vacio"}

        res = self.__conector.update("menu",
                                     ["nombre", "foto", "precio, fk_restaurante"],
                                     " id_menu=%(id_menu)s ",
                                     {"nombre": nombre, "foto": foto, "precio": precio, "fk_restaurante": id_restaurante,
                                      "id_menu": id_menu})

        if res['success'] == True:
            self.__conector.commit()

        return res

    def eliminar(self, id_menu):
        if id_menu == '':
            return {'success': False, 'error': "Id menu vacio"}

        res = self.__conector.delete("menu",
                    " id_menu=%(id_menu)s ",
                    {"id_menu" : id_menu} )

        if res['success'] == True:
            self.__conector.commit()

        return res