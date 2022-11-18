from app.objetos_sesion.Ingrediente import Ingrediente

class IngredienteBase(Ingrediente):

    def __init__(self, idIngrediente, nombre, foto, undMedida, idIngredienteBase, ingredientesCambio, cantidadPorUnidad, autoSelect):
        super().__init__(idIngrediente,nombre,foto,undMedida)
        self.__idIngredienteBase = idIngredienteBase
        self.__ingredientesCambio = ingredientesCambio
        self.__cantidadPorUnidad = cantidadPorUnidad
        self.__autoSelect = autoSelect

    def getIdIngredienteBase(self):
        return self.__idIngredienteBase

    def setIdIngredienteBase(self, value):
        self.__idIngredienteBase = value

    def getIngredientesCambio(self):
        return self.__ingredientesCambio

    def setIngredientesCambio(self, value):
        self.__ingredientesCambio = value

    def getCantidadPorUnidad(self):
        return self.__cantidadPorUnidad

    def setCantidadPorUnidad(self, value):
        self.__cantidadPorUnidad = value

    def getAutoSelect(self):
        return self.__autoSelect

    def setAutoSelect(self, value):
        self.__autoSelect = value

