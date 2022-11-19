from app.logica.IngredienteControlador import IngredienteControlador

class Ingrediente:

    def __init__(self, idIngrediente, nombre, foto, undMedida):
        self.__idIngrediente = idIngrediente
        self.__nombre = nombre
        self.__foto = foto
        self.__undMedida = undMedida

        self.__ingredienteControlador = IngredienteControlador()

    def setBdInfoIngrediente(self, id):
        infoIngrediente = self.__ingredienteControlador.obtener_x_id(id)
        if infoIngrediente:
            infoIngrediente = infoIngrediente[0]
            self.__idIngrediente = infoIngrediente['id_ingrediente']
            self.__nombre = infoIngrediente['nombre']
            self.__foto = infoIngrediente['foto']
            self.__undMedida = infoIngrediente['und_medida']

    def getIdIngrediente(self):
        return self.__idIngrediente

    def setIdIngrediente(self, value):
        self.__idIngrediente = value

    def getNombre(self):
        return self.__nombre

    def setNombre(self, value):
        self.__nombre = value

    def getFoto(self):
        return self.__foto

    def setFoto(self, value):
        self.__foto = value

    def getUndMedida(self):
        return self.__undMedida

    def setUndMedida(self, value):
        self.__undMedida = value
