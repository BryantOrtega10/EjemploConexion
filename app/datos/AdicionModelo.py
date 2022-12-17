from app.datos.MysqlConnector import MysqlConnection

class AdicionModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_ingrediente, cantidad, maximo):
        if cantidad == '':
            return {'success': False, 'error': 'Cantidad vacia'}
        if maximo == '':
            return {'success': False, 'error': 'Maximo vacio'}

        res = self.__conector.insert('adicion', {'fk_ingrediente': id_ingrediente, 'cantidad': cantidad, 'maximo': maximo})
        if res['success'] == True:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=['adicion'], limit=limite)
        return res

    def obtenerUno(self, id):
        res = self.__conector.select(tables=['adicion'], where=' id_adicion=%(id_adicion)s', values={'id_adicion':id})
        return res

    def modificar(self, id_adicion, id_ingrediente, cantidad, maximo):
        if cantidad == '':
            return {'success': False, 'error': 'Cantidad vacia'}
        if maximo == '':
            return {'success': False, 'error': 'Maximo vacio'}
        if id_adicion == '':
            return {'success': False, 'error': 'Id adicion vacio'}

        res = self.__conector.update('adicion',
                    ['cantidad', 'id_ingrediente', 'maximo'],
                     'id_adicion=%(id_adicion)s',
                    {'cantidad': cantidad, 'id_ingrediente': id_ingrediente, 'maximo': maximo, 'id_adicion' : id_adicion})

        if res['success'] == True:
            self.__conector.commit()


        return res

    def eliminar(self, id_adicion):
        if id_adicion == '':
            return {'success': False, 'error': 'Id adicion vacio'}

        res = self.__conector.delete('adicion',
                    'id_adicion=%(id_adicion)s',
                    {'id_adicion': id_adicion})

        if res['success'] == True:
            self.__conector.commit()

        return res
