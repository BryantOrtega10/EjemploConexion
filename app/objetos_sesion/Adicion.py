from app.objetos_sesion.Ingrediente import Ingrediente
from app.logica.IngredienteControlador import IngredienteControlador
from app.logica.AdicionControlador import AdicionControlador


class Adicion(Ingrediente):

    def __init__(self, idIngrediente="", nombre="", foto="",  undMedida="", idAdicion="", cantidadPorUnidad="", maximo="", precio=""):
        super().__init__(idIngrediente, nombre, foto, undMedida)
        self.__idAdicion = idAdicion
        self.__cantidadPorUnidad = cantidadPorUnidad
        self.__maximo = maximo
        self.__precio = precio

        self.__adicionControlador = AdicionControlador()

    def setBdInfoAdicion(self, id_adicion):
        infoAdicion = self.__adicionControlador.obtener_x_id(id_adicion)
        if infoAdicion:
            infoAdicion = infoAdicion[0]
            self.__idAdicion = infoAdicion["id_adicion"]
            self.__cantidadPorUnidad = infoAdicion['cantidad']
            self.__maximo = infoAdicion['maximo']
            self.__precio = infoAdicion['precio']
            self.setBdInfoIngrediente(infoAdicion['fk_ingrediente'])

    def getIdAdicion(self):
        return self.__idAdicion

    def setIdAdicion(self, value):
        self.__idAdicion = value

    def getCantidadPorUnidad(self):
        return self.__cantidadPorUnidad

    def setCantidadPorUnidad(self, value):
        self.__cantidadPorUnidad = value

    def getMaximo(self):
        return self.__maximo

    def setMaximo(self, value):
        self.__maximo = value

    def getPrecio(self):
        return self.__precio

    def setPrecio(self, value):
        self.__precio = value


