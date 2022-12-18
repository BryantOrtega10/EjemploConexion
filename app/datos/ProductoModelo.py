from app.datos.MysqlConnector import MysqlConnection


class ProductoModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, nombre, precio, tipo, foto, maximo_ingredientes_base, aplica_maximo, minimo_ingredientes_base,
                aplica_minimo, id_restaurante):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f"{keys[i]} vacio"}

        res = self.__conector.insert("producto", {"nombre": nombre, "precio": precio, "tipo": tipo, "foto": foto,
                                                  "maximo_ingredientes_base": maximo_ingredientes_base,
                                                  "aplica_maximo": aplica_maximo,
                                                  "minimo_ingredientes_base": minimo_ingredientes_base,
                                                  "aplica_minimo": aplica_minimo, "id_restaurante": id_restaurante})
        if res['success'] == True:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=["producto"], limit=limite)
        return res

    def obtener_x_rest(self, fk_restaurante, limite=None):
        res = self.__conector.select(tables=["producto"], where=' fk_restaurante=%(fk_restaurante)s', values={"fk_restaurante":fk_restaurante}, limit=limite)
        return res
    
    def obtenerUno(self, id):
        res = self.__conector.select(tables=["producto"], where=' id_producto=%(id_producto)s',
                                     values={"id_producto": id})
        return res

    def modificar(self, id_producto, nombre, precio, tipo, foto, maximo_ingredientes_base, aplica_maximo,
                  minimo_ingredientes_base, aplica_minimo, id_restaurante):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f"{keys[i]} vacio"}

        res = self.__conector.update("producto",
                                     ["nombre", "precio", "tipo", "foto", "maximo_ingredientes_base", "aplica_maximo",
                                      "minimo_ingredientes_base", "aplica_minimo", "id_restaurante"],
                                     " id_producto=%(id_producto)s ",
                                     {"nombre": nombre, "precio": precio, "tipo": tipo, "foto": foto,
                                      "maximo_ingredientes_base": maximo_ingredientes_base,
                                      "aplica_maximo": aplica_maximo,
                                      "minimo_ingredientes_base": minimo_ingredientes_base,
                                      "aplica_minimo": aplica_minimo, "id_restaurante": id_restaurante,
                                      "id_producto": id_producto})

        if res['success'] == True:
            self.__conector.commit()

        return res

    def eliminar(self, id_producto):
        if id_producto == '':
            return {'success': False, 'error': "Id producto vacio"}

        res = self.__conector.delete("producto",
                                     " id_producto=%(id_producto)s ",
                                     {"id_producto": id_producto})

        if res['success'] == True:
            self.__conector.commit()

        return res
