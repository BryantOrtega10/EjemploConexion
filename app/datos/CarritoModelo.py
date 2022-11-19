from app.datos.MysqlConnector import MysqlConnection


class CarritoModelo:

    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, sub_total, fecha_creacion, fecha_finalizacion, estado, id_cliente):
        if sub_total == "":
            return {'success': False, 'error': "Sub total vacio"}
        if fecha_creacion == "":
            return {'success': False, 'error': "Fecha de creacion vacia"}

        res = self.__conector.insert("carrito", {"sub_total": sub_total, "fecha_creacion": fecha_creacion, "fecha_finalizacion": fecha_finalizacion,
                                                 "estado": estado, "fk_cliente": id_cliente})
        if res["success"] == True:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=["carrito"], limit=limite)
        return res

    def obtenerUno(self, id):
        res = self.__conector.select(tables=["carrito"], where=' id_carrito=%(id_carrito)s',
                                     values={"id_carrito": id})
        return res

    def modificar(self, id_carrito, sub_total, fecha_creacion, fecha_finalizacion, estado, id_cliente):
        if sub_total == "":
            return {'success': False, 'error': "Sub total vacio"}
        if fecha_creacion == "":
            return {'success': False, 'error': "Fecha de creacion vacia"}

        res = self.__conector.update("carrito",
                                     ["sub_total", "fecha_creacion", "fecha_finalizacion", "estado", "id_cliente"],
                                     " id_carrito=%(id_carrito)s ",
                                     {"sub_total": sub_total, "fecha_creacion": fecha_creacion, "fecha_finalizacion": fecha_finalizacion,
                                      "estado": estado, "id_cliente": id_cliente, "id_carrito": id_carrito})

        if res["success"] == True:
            self.__conector.commit()

        return res

    def eliminar(self, id_carrito):
        if id_carrito == "":
            return {'success': False, 'error': "Id carrito vacio"}

        res = self.__conector.delete("carrito",
                                     " id_carrito=%(id_carrito)s ",
                                     {"id_carrito": id_carrito})

        if res["success"] == True:
            self.__conector.commit()

        return res