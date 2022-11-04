from app.datos.IngredienteModelo import Ingrediente

class IngredienteControlador:

    def __init__(self):
        self.__modelo = Ingrediente()


    def lista_ingredientes(self):
        ingredientes = self.__modelo.obtener_ingredientes(2)
        return ingredientes