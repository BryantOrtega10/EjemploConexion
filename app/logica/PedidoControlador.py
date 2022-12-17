from app.datos.PedidoModelo import PedidoModelo

class PedidoControlador:

    def __init__(self):
        self.__modelo = PedidoModelo()

    def lista(self):
        pedidos = self.__modelo.obtener()
        return pedidos

    def obtener_x_id(self, id):
        pedido = self.__modelo.obtenerUno(id)
        return pedido

    def agregar(self):
        pass

    def modificar(self):
        pass

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res