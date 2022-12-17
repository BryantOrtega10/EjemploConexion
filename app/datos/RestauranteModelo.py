from app.datos.MysqlConnector import MysqlConnection


class RestauranteModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_restaurante, nombre, logo, en_servicio, especialidad):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f'{keys[i]} vacio'}

        res = self.__conector.insert(table='restaurante', insert={'id_restaurante': id_restaurante, 'nombre': nombre, 'logo': logo, 'en_servicio': en_servicio, 'especialidad': especialidad})

        if res['success']:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=['restaurante'], limit=limite)
        return res

    def obtenerUno(self, id):
        res = self.__conector.select(tables=['restaurante'], where='id_restaurante=%(id_restaurante)s', values={'id_restaurante': id})
        return res

    def modificar(self, id_restaurante, nombre, logo, en_servicio, especialidad):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f"{keys[i]} vacio"}

        res = self.__conector.update(table='restaurante', update=['nombre', 'logo', 'en_servicio', 'en_servicio'],
                                     where='id_restaurante=%(id_restaurante)s',
                                     values={'nombre': nombre, 'logo': logo,
                                             'en_servicio': en_servicio, 'especialidad': especialidad, 'id_restaurante': id_restaurante})
        if res['success'] == True:
            self.__conector.commit()

        return res

    def eliminar(self, id_restaurante):
        if id_restaurante == '':
            return {'success': False, 'error': 'Id sede vacio'}

        res = self.__conector.delete(table='restaurante',
                                     where='id_restaurante=%(id_restaurante)s',
                                     values={'id_restaurante': id_restaurante})

        if res['success'] == True:
            self.__conector.commit()

        return res
