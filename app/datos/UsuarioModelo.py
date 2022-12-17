from app.datos.MysqlConnector import MysqlConnection


class UsuarioModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_usuario, user, password, rol):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f'{keys[i]} vacio'}

        res = self.__conector.insert(table='usuario',
                                     insert={'id_usuario': id_usuario, 'user': user, 'password': password, 'rol': rol})

        if res['success']:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=['usuario'], limit=limite)
        return res

    def obtenerUno(self, id):
        res = self.__conector.select(tables=['usuario'], where='id_usuario=%(id_usuario)s', values={'id_usuario': id})
        return res

    def modificar(self, id_usuario, user, password, rol):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f"{keys[i]} vacio"}

        res = self.__conector.update(table='usuario', update=['user', 'password', 'rol'],
                                     where='id_usuario=%(id_usuario)s',
                                     values={'user': user, 'password': password,
                                             'rol': rol, 'id_usuario': id_usuario})
        if res['success']:
            self.__conector.commit()

        return res

    def eliminar(self, id_usuario):
        if id_usuario == '':
            return {'success': False, 'error': 'Id sede vacio'}

        res = self.__conector.delete(table='usuario',
                                     where='id_usuario=%(id_usuario)s',
                                     values={'id_usuario': id_usuario})

        if res['success']:
            self.__conector.commit()

        return res
