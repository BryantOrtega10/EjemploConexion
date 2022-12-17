from app.datos.MysqlConnector import MysqlConnection


class ClienteModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_cliente, documento, nombre, apellido, foto, direccion, email, fk_usuario):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f'{keys[i]} vacio'}

        res = self.__conector.insert(table='cliente',
                                     insert={'id_cliente': id_cliente, 'documento': documento, 'nombre': nombre,
                                             'apellido': apellido, 'foto': foto, 'direccion': direccion, 'email': email,
                                             'fk_usuario': fk_usuario})

        if res['success']:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=['cliente'], limit=limite)
        return res

    def obtenerUno(self, id):
        res = self.__conector.select(tables=['cliente'], where='id_cliente=%(id_cliente)s', values={'id_cliente': id})
        return res

    def modificar(self, id_cliente,documento, nombre, apellido, foto, direccion, email, fk_usuario):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f"{keys[i]} vacio"}

        res = self.__conector.update(table='cliente',
                                     update=['documento', 'nombre', 'apellido', 'foto', 'direccion', 'email',
                                             'fk_usuario'],
                                     where='id_cliente=%(id_cliente)s',
                                     values={'documento': documento, 'nombre': nombre, 'apellido': apellido,
                                             'foto': foto, 'direccion': direccion, 'email': email,
                                             'fk_usuario': fk_usuario, 'id_cliente': id_cliente})
        if res['success']:
            self.__conector.commit()

        return res

    def eliminar(self, id_cliente):
        if id_cliente == '':
            return {'success': False, 'error': 'Id sede vacio'}

        res = self.__conector.delete(table='cliente',
                                     where='id_cliente=%(id_cliente)s',
                                     values={'id_cliente': id_cliente})

        if res['success']:
            self.__conector.commit()

        return res
