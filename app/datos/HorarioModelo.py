from app.datos.MysqlConnector import MysqlConnection


class HorarioModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, id_horario, dia, hora_inicio, minuto_inicio, hora_fin, minuto_fin, fk_restaurante):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f'{keys[i]} vacio'}

        res = self.__conector.insert(table='horario',
                                     insert={'id_horario': id_horario, 'dia': dia, 'hora_inicio': hora_inicio,
                                             'minuto_inicio': minuto_inicio, 'hora_fin': hora_fin,
                                             'minuto_fin': minuto_fin, 'fk_restaurante': fk_restaurante})

        if res['success']:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=['horario'], limit=limite)
        return res

    def obtenerUno(self, id):
        res = self.__conector.select(tables=['horario'], where='id_horario=%(id_horario)s', values={'id_horario': id})
        return res

    def modificar(self, id_horario, dia, hora_inicio, minuto_inicio, hora_fin, minuto_fin, fk_restaurante):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f"{keys[i]} vacio"}

        res = self.__conector.update(table='horario',
                                     update=['dia', 'hora_inicio', 'minuto_inicio', 'hora_fin', 'minuto_fin',
                                             'fk_restaurante'],
                                     where='id_horario=%(id_horario)s',
                                     values={'dia': dia, 'hora_inicio': hora_inicio, 'minuto_inicio': minuto_inicio,
                                             'hora_fin': hora_fin, 'minuto_fin': minuto_fin,
                                             'fk_restaurante': fk_restaurante, 'id_horario': id_horario})
        if res['success']:
            self.__conector.commit()

        return res

    def eliminar(self, id_horario):
        if id_horario == '':
            return {'success': False, 'error': 'Id sede vacio'}

        res = self.__conector.delete(table='horario',
                                     where='id_horario=%(id_horario)s',
                                     values={'id_horario': id_horario})

        if res['success']:
            self.__conector.commit()

        return res
