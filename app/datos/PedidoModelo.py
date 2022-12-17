from app.datos.MysqlConnector import MysqlConnection


class PedidoModelo:
    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar(self, idpedido , estado, metodo_pago, total, fk_carrito):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f'{keys[i]} vacio'}

        res = self.__conector.insert(table='pedido',
                                     insert={'idpedido': idpedido, 'estado': estado, 'metodo_pago': metodo_pago,
                                             'total': total, 'fk_carrito': fk_carrito})

        if res['success']:
            self.__conector.commit()

        return res

    def obtener(self, limite=None):
        res = self.__conector.select(tables=['pedido'], limit=limite)
        return res

    def obtenerUno(self, id):
        res = self.__conector.select(tables=['pedido'], where='idpedido=%(idpedido)s', values={'idpedido': id})
        return res

    def modificar(self, idpedido , estado, metodo_pago, total, fk_carrito):
        rows = locals()
        keys = list(rows.keys())
        values = list(rows.values())
        for (i, item) in enumerate(values):
            if item == '':
                return {'success': False, 'error': f"{keys[i]} vacio"}

        res = self.__conector.update(table='pedido',
                                     update=['estado', 'metodo_pago', 'total', 'fk_carrito'],
                                     where='idpedido=%(idpedido)s',
                                     values={'estado': estado, 'metodo_pago': metodo_pago, 'total': total,
                                             'fk_carrito': fk_carrito, 'idpedido': idpedido})
        if res['success']:
            self.__conector.commit()

        return res

    def eliminar(self, idpedido):
        if idpedido == '':
            return {'success': False, 'error': 'Id sede vacio'}

        res = self.__conector.delete(table='cliente',
                                     where='idpedido=%(idpedido)s',
                                     values={'idpedido': idpedido})

        if res['success']:
            self.__conector.commit()

        return res
