from app.objetos_sesion.Ingrediente import Ingrediente

class IngredienteBase(Ingrediente):

    def __init__(self,idIngrediente,nombre,foto,undMedida,idIngredienteBase,ingredientesCambio,cantidadPorUnidad, autoSelect):
        super().__init__(idIngrediente,nombre,foto,undMedida)
        self.__idIngredienteBase = idIngredienteBase
        self.__ingredientesCambio = ingredientesCambio
        self.__cantidadPorUnidad = cantidadPorUnidad
        self.__autoSelect = autoSelect
