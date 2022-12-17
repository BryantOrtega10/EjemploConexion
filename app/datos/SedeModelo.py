from app.datos.MysqlConnector import MysqlConnection


class SedeModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_sede, fk_restaurante, fk_usuario, direccion):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f'{keys[i]} vacio'}

        res = self.__conector.insert('sede', {'id_sede': id_sede, 'fk_restaurante': fk_restaurante,
                                              'fk_usuario': fk_usuario, 'direccion': direccion})
        if res['success']:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=['sede'], limit=limite)
        return res

    def obtenerUno(self, id):
        res = self.__conector.select(tables=['sede'], where='id_sede=%(id_sede)s', values={'id_sede': id})
        return res

    def modificar(self, id_sede, fk_restaurante, fk_usuario, direccion):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f"{keys[i]} vacio"}

        res = self.__conector.update(table='sede', update=['fk_restaurante', 'fk_usuario', 'direccion'],
                                     where='id_sede=%(id_sede)s',
                                     values={'fk_restaurante': fk_restaurante, 'fk_usuario': fk_usuario,
                                             'direccion': direccion, 'id_sede': id_sede})
        if res['success']:
            self.__conector.commit()

        return res

    def eliminar(self, id_sede):
        if id_sede == '':
            return {'success': False, 'error': 'Id sede vacio'}

        res = self.__conector.delete(table='sede',
                                     where='id_sede=%(id_sede)s',
                                     values={'id_sede': id_sede})

        if res['success'] == True:
            self.__conector.commit()

        return res
