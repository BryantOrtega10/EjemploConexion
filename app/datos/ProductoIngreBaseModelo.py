from app.datos.MysqlConnector import MysqlConnection


class ProductoIngredienteBaseModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_producto, id_ingrediente_base, auto_select):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f"{keys[i]} vacio"}

        res = self.__conector.insert("producto_ingrediente_base", {"fk_producto": id_producto,
                                                                   "fk_ingrediente_base": id_ingrediente_base,
                                                                   "auto_select": auto_select})

        if res['success'] == True:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=["producto_ingrediente_base"], limit=limite)
        return res

    def obtenerUno(self, id_producto, id_ingrediente_base):
        pass

    def obtenerFKIngredientesBase(self, id_producto):
        if id_producto != '':
            res = self.__conector.select(fields=["producto_ingrediente_base.fk_ingrediente_base", 
                                                 "producto_ingrediente_base.auto_select", 
                                                 "ingrediente_base.cantidad",
                                                 "ingrediente.*"],
                                         tables=["producto_ingrediente_base", "ingrediente_base", "ingrediente"],
                                         where="producto_ingrediente_base.fk_ingrediente_base = ingrediente_base.id_ingrediente_base and "\
                                               "ingrediente_base.fk_ingrediente = ingrediente.id_ingrediente and "\
                                               "producto_ingrediente_base.fk_producto=%(id_producto)s",
                                         values={"id_producto": id_producto})
            return res

    def modificar(self):
        pass

    def eliminar(self):
        pass
