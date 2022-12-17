from app.datos.MysqlConnector import MysqlConnection

class IngredienteBaseModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, cantidad, id_ingrediente):
        if cantidad == '':
            return {'success': False, 'error': 'Cantidad vacia'}
        if id_ingrediente == 'success':
            return {'success': False, 'error': 'Id ingrediente vacio'}

        res = self.__conector.insert('ingrediente_base', {'cantidad': cantidad, 'id_ingrediente': id_ingrediente})
        if res['success'] == True:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=['ingrediente_base'], limit=limite)
        return res

    def obtenerUno(self, id):
        res = self.__conector.select(tables=['ingrediente_base'], where='id_ingrediente_base=%(id_ingrediente_base)s',
                                     values={'id_ingrediente_base': id})
        return res

    def modificar(self, id_ingrediente_base, cantidad, id_ingrediente):
        if id_ingrediente_base == '':
            return {'success': False, 'error': 'Id ingrediente base vacio'}
        if cantidad == '':
            return {'success': False, 'error': 'Cantidad vacia'}
        if id_ingrediente == '':
            return {'success': False, 'error': 'Id ingrediente vacio'}

        res = self.__conector.update('ingrediente_base',
                                     ['cantidad', 'id_ingrediente'],
                                     'id_ingrediente_base=%(id_ingrediente_base)s',
                                     {'cantidad': cantidad, 'id_ingrediente': id_ingrediente,
                                      'id_ingrediente_base': id_ingrediente_base})

        if res['success'] == True:
            self.__conector.commit()

        return res

    def eliminar(self, id_ingrediente_base):
        if id_ingrediente_base == '':
            return {'success': False, 'error': 'Id ingrediente base vacio'}

        res = self.__conector.delete('ingrediente_base',
                                     'id_ingrediente_base=%(id_ingrediente_base)s',
                                     {'id_ingrediente_base': id_ingrediente_base})

        if res['success'] == True:
            self.__conector.commit()

        return res