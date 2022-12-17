from app.datos.MysqlConnector import MysqlConnection


class AdminTecnicoModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_admin_tecnico, documento, nombre, apellido, email, fk_usuario):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f'{keys[i]} vacio'}

        res = self.__conector.insert(table='admin_tecnico',
                                     insert={'id_admin_tecnico': id_admin_tecnico, 'documento': documento,
                                             'nombre': nombre,
                                             'apellido': apellido, 'email': email, 'fk_usuario': fk_usuario})

        if res['success']:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=['admin_tecnico'], limit=limite)
        return res

    def obtenerUno(self, id):
        res = self.__conector.select(tables=['admin_tecnico'], where='id_admin_tecnico=%(id_admin_tecnico)s',
                                     values={'id_admin_tecnico': id})
        return res

    def modificar(self, id_admin_tecnico, documento, nombre, apellido, email, fk_usuario):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f"{keys[i]} vacio"}

        res = self.__conector.update(table='admin_tecnico',
                                     update=['documento', 'nombre', 'apellido', 'email', 'fk_usuario'],
                                     where='id_admin_tecnico=%(id_admin_tecnico)s',
                                     values={'documento': documento, 'nombre': nombre, 'apellido': apellido,
                                             'email': email, 'fk_usuario': fk_usuario,
                                             'id_admin_tecnico': id_admin_tecnico})
        if res['success']:
            self.__conector.commit()

        return res

    def eliminar(self, id_admin_tecnico):
        if id_admin_tecnico == '':
            return {'success': False, 'error': 'Id sede vacio'}

        res = self.__conector.delete(table='admin_tecnico',
                                     where='id_admin_tecnico=%(id_admin_tecnico)s',
                                     values={'id_admin_tecnico': id_admin_tecnico})

        if res['success']:
            self.__conector.commit()

        return res
