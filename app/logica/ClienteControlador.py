from app.datos.ClienteModelo import ClienteModelo

class ClienteControlador:

    def __init__(self):
        self.__modelo = ClienteModelo()

    def lista(self):
        clientes = self.__modelo.obtener()
        return clientes

    def obtener_x_id(self, id):
        cliente = self.__modelo.obtenerUno(id)
        return cliente

    def agregar(self):
        pass

    def modificar(self):
        pass

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res