from app.datos.MysqlConnector import MysqlConnection


class IngredienteModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, nombre, foto, und_medida):
        if nombre == '':
            return {'success': False, 'error': 'Nombre vacio'}
        if und_medida == '':
            return {'success': False, 'error': 'Unidad de medida vacio'}

        res = self.__conector.insert('ingrediente', {'nombre': nombre, 'foto': foto, 'und_medida': und_medida})
        if res['success'] == True:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=['ingrediente'], limit=limite)
        return res

    def obtenerUno(self, id):
        res = self.__conector.select(tables=['ingrediente'], where='id_ingrediente=%(id_ingrediente)s',
                                     values={'id_ingrediente': id})
        return res

    def modificar(self, nombre, foto, und_medida, id_ingrediente):
        if nombre == '':
            return {'success': False, 'error': 'Nombre vacio'}
        if und_medida == '':
            return {'success': False, 'error': 'Unidad de medida vacio'}
        if id_ingrediente == '':
            return {'success': False, 'error': 'Id ingrediente vacio'}

        res = self.__conector.update('ingrediente',
                                     ['nombre', 'und_medida', 'foto'],
                                     'id_ingrediente=%(id_ingrediente)s',
                                     {'nombre': nombre, 'foto': foto, 'und_medida': und_medida,
                                      'id_ingrediente': id_ingrediente})

        if res['success'] == True:
            self.__conector.commit()

        return res

    def eliminar(self, id_ingrediente):
        if id_ingrediente == '':
            return {'success': False, 'error': 'Id ingrediente vacio'}

        res = self.__conector.delete('ingrediente',
                                     'id_ingrediente=%(id_ingrediente)s',
                                     {'id_ingrediente': id_ingrediente})

        if res['success']:
            self.__conector.commit()

        return res
