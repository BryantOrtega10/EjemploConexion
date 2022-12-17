from app.datos.HorarioModelo import HorarioModelo

class HorarioControlador:

    def __init__(self):
        self.__modelo = HorarioModelo()

    def lista(self):
        horarios = self.__modelo.obtener()
        return horarios

    def obtener_x_id(self, id):
        horario = self.__modelo.obtenerUno(id)
        return horario

    def agregar(self):
        pass

    def modificar(self):
        pass

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res