from app.logica.IngredienteBaseControlador import IngredienteBaseControlador
from app.objetos_sesion.Ingrediente import Ingrediente


class IngredienteBase(Ingrediente):

    def __init__(self, idIngrediente="", nombre="", foto="", undMedida="", idIngredienteBase="", cantidadPorUnidad="", autoSelect=""):
        super().__init__(idIngrediente,nombre,foto,undMedida)
        self.__idIngredienteBase = idIngredienteBase
        self.__cantidadPorUnidad = cantidadPorUnidad
        self.__autoSelect = autoSelect

        self.__ingredienteBaseControlador = IngredienteBaseControlador()

    def setBdInfoIngredienteBase(self, id_ingrediente_base, auto_select):
        infoIngredienteBase = self.__ingredienteBaseControlador.obtener_x_id(id_ingrediente_base)
        if infoIngredienteBase:
            infoIngredienteBase = infoIngredienteBase[0]
            self.__idIngredienteBase = infoIngredienteBase['id_ingrediente_base']
            self.__cantidadPorUnidad = infoIngredienteBase['cantidad']
            self.__autoSelect = auto_select
            self.setBdInfoIngrediente(infoIngredienteBase['fk_ingrediente'])


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

