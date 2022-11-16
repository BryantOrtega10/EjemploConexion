from app.objetos_sesion.Ingrediente import Ingrediente


class Adicion(Ingrediente):

    def __init__(self, idIngrediente, nombre, foto,  undMedida, idAdicion, cantidadPorUnidad, maximo, precio):
        super().__init__(idIngrediente, nombre,foto, undMedida)
        self.__idAdicion = idAdicion
        self.__cantidadPorUnidad = cantidadPorUnidad
        self.__maximo = maximo
        self.__precio = precio

    def getPrecio(self):
        return self.__precio
