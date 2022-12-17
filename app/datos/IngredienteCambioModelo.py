from app.datos.MysqlConnector import MysqlConnection


class IngredienteCambioModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_ingrediente_base, id_ingrediente_cambio):
        if id_ingrediente_base == '':
            return {'success': False, 'error': 'Id de ingrediente base vacio'}
        if id_ingrediente_cambio == '':
            return {'success': False, 'error': 'Id de ingrediente cambio vacio'}

        res = self.__conector.insert('ingrediente_cambio', {'id_ingrediente_base': id_ingrediente_base,
                                                            'id_ingrediente_cambio': id_ingrediente_cambio})
        if res['success'] == True:
            self.__conector.commit()

        return res

    def obtenerFKIngredientesDeCambio(self, id_ingrediente):
        if id_ingrediente != '':
            return self.__conector.select(fields=['fk_ingrediente_cambio'],
                                          tables=['ingrediente_cambio'],
                                          where='fk_ingrediente_base=%(id_ingrediente)s',
                                          values={'id_ingrediente': id_ingrediente})
        else:
            return {'success': False, 'error': 'Id de ingrediente vacio'}
