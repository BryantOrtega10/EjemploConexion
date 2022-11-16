class Producto:
    
    def __init__(self, idProducto, nombre, precio, foto, tipoProducto, ingredientes, ingredientesSeleccionados, adiciones, adicionesSeleccionadas, maxIngBase, aplicaMax, minIngBase, aplicaMin):
        self.__idProducto = idProducto
        self.__nombre = nombre
        self.__precio = precio
        self.__foto = foto
        self.__tipoProducto = tipoProducto
        self.__ingredientes = ingredientes
        self.__ingredientesSeleccionados = ingredientesSeleccionados
        self.__adiciones = adiciones
        self.__adicionesSeleccionadas = adicionesSeleccionadas
        self.__maxIngBase = maxIngBase
        self.__aplicaMax = aplicaMax
        self.__minIngBase = minIngBase
        self.__aplicaMin = aplicaMin


    def getIdProducto(self):
        return self.__idProducto

    def getPrecio(self):
        return self.__precio

    def getAdicionesSeleccionadas(self):
        return self.__adicionesSeleccionadas