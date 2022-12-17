from app.logica.PedidoControlador import PedidoControlador

class Pedido:
    def __init__(self, id_pedido , estado, metodo_pago, total, carritos=[]):
        self.__id = id_pedido
        self.__estado = estado
        self.__metodo_pago = metodo_pago
        self.__total = total
        self.__carritos = carritos

    def getId(self):
        return self.__id

    def setId(self, value):
        self.__id = value

    def getEstado(self):
        return self.__estado

    def setEstado(self, value):
        self.__estado = value

    def getMetodoPago(self):
        return self.__metodo_pago

    def setMetodoPago(self, value):
        self.__metodo_pago = value

    def getTotal(self):
        return self.__total

    def setTotal(self, value):
        self.__total = value

    def getCarritos(self):
        return self.__carritos

    def setCarritos(self, value):
        self.__carritos = value
