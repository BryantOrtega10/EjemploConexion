from app.datos.MysqlConnector import MysqlConnection


class SedeIngredienteModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_sede, id_ingrediente, stock):
        res = self.__conector.insert("sede_ingrediente", {"fk_sede": id_sede,
                                                          "fk_ingrediente": id_ingrediente,
                                                          'stock': stock})
        if res['success'] == True:
            self.__conector.commit()

        return res

    # Trae la informacion de los ingredientes  relacionados con una sede
    def obtenerInfoIngredientes(self, id_sede):
        if id_sede != '':
            res = self.__conector.select(fields=["fk_ingrediente", 'stock'],
                                         tables=["sede_ingrediente"],
                                         where="fk_sede=%(id_sede)s",
                                         values={"id_sede": id_sede})
            return res
