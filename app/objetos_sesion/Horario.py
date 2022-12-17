from app.logica.HorarioControlador import HorarioControlador


class Horario:
    def __init__(self, id_horario='', dia='', hora_inicio='', minuto_inicio='', hora_fin='', minuto_fin=''):
        self.__id = id_horario
        self.__dia = dia
        self.__hora_inicio = hora_inicio
        self.__minuto_inicio = minuto_inicio
        self.__hora_fin = hora_fin
        self.__minuto_fin = minuto_fin

        self.__sedeControlador = HorarioControlador()

    def getId(self):
        return self.__id

    def setId(self, value):
        self.__id = value

    def getDia(self):
        return self.__dia

    def setDia(self, value):
        self.__dia = value

    def getHoraInicio(self):
        return self.__hora_inicio

    def setHoraInicio(self, value):
        self.__hora_inicio = value

    def getMinutoInicio(self):
        return self.__minuto_inicio

    def setMinutoInicio(self, value):
        self.__minuto_inicio = value

    def getHoraFin(self):
        return self.__hora_fin

    def setHoraFin(self, value):
        self.__hora_fin = value

    def getMinutoFin(self):
        return self.__minuto_fin

    def setMinutoFin(self, value):
        self.__minuto_fin = value