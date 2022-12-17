from app.datos.MysqlConnector import MysqlConnection


class ProductoAdicionModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_producto, id_adicion, precio):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f"{keys[i]} vacio"}

        res = self.__conector.insert("producto_ingrediente_base", {"fk_producto": id_producto,
                                                                   "fk_adicion": id_adicion,
                                                                   "precio": precio})
        if res['success'] == True:
            self.__conector.commit()

        return res

    def obtenerFKAdiciones(self, id_producto):
        if id_producto != '':
            res = self.__conector.select(fields=["fk_adicion, precio"],
                                         tables=["producto_adicion"],
                                         where="fk_producto=%(id_producto)s",
                                         values={"id_producto": id_producto})
            return res