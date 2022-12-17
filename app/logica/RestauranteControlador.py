from app.datos.RestauranteModelo import RestauranteModelo

class RestauranteControlador:

    def __init__(self):
        self.__modelo = RestauranteModelo()

    def lista(self):
        restaurantes = self.__modelo.obtener()
        return restaurantes

    def obtener_x_id(self, id):
        restaurante = self.__modelo.obtenerUno(id)
        return restaurante

    def agregar(self):
        pass

    def modificar(self):
        pass

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res