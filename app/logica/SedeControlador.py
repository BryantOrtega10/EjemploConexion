from app.datos.SedeModelo import SedeModelo

class SedeControlador:

    def __init__(self):
        self.__modelo = SedeModelo()

    def lista(self):
        sedes = self.__modelo.obtener()
        return sedes

    def obtener_x_id(self, id):
        sede = self.__modelo.obtenerUno(id)
        return sede

    def agregar(self):
        pass

    def modificar(self):
        pass

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res