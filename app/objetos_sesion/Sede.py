from app.logica.SedeControlador import SedeControlador


class Sede:
    def __init__(self, id_sede='', usuario=None, direccion='', ingredientes=[]):
        self.__id = id_sede
        self.__usuario = usuario
        self.__direccion = direccion
        self.__ingredientes = ingredientes

        self.__sedeControlador = SedeControlador()

    def getId(self):
        return self.__id

    def setId(self, value):
        self.__id = value

    def getUsuario(self):
        return self.__usuario

    def setUsuario(self, value):
        self.__usuario = value

    def getDireccion(self):
        return self.__direccion

    def setDireccion(self, value):
        self.__direccion = value

    def getIngredientes(self):
        return self.__ingredientes

    def setIngredientes(self, value):
        self.__ingredientes = value
