from app.logica.ProductoControlador import ProductoControlador

class Producto:
    
    def __init__(self, idProducto="", nombre="", precio=0, foto="", tipoProducto="", ingredientes=[], ingredientesSeleccionados=[], adiciones=[], adicionesSeleccionadas=[], maxIngBase="", aplicaMax="", minIngBase="", aplicaMin=""):
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

        self.__productoControlador = ProductoControlador()

    def setBdInfoProducto(self, id):
        infoProducto = self.__productoControlador.obtener_x_id(id)
        if infoProducto:
            infoProducto = infoProducto[0]
            self.__idProducto = infoProducto['id_producto']
            self.__nombre = infoProducto['nombre']
            self.__precio = infoProducto['precio']
            self.__tipoProducto = infoProducto['tipo']
            self.__foto = infoProducto['foto']
            self.__maxIngBase = infoProducto['maximo_ingredientes_base']
            self.__aplicaMax = infoProducto['aplica_maximo']
            self.__minIngBase = infoProducto['minimo_ingredientes_base']
            self.__aplicaMin = infoProducto['aplica_minimo']


    def getIdProducto(self):
        return self.__idProducto

    def setIdProducto(self, value):
        self.__idProducto = value

    def getNombre(self):
        return self.__nombre

    def setNombre(self, value):
        self.__nombre = value

    def getPrecio(self):
        return self.__precio

    def setPrecio(self, value):
        self.__precio = value

    def getFoto(self):
        return self.__foto

    def setFoto(self, value):
        self.__foto = value

    def getTipoProducto(self):
        return self.__tipoProducto

    def setTipoProducto(self, value):
        self.__tipoProducto = value

    def getIngredientes(self):
        return self.__ingredientes

    def setIngredientes(self, value):
        self.__ingredientes = value

    def getIngredientesSeleccionados(self):
        return self.__ingredientesSeleccionados

    def setIngredientesSeleccionados(self, value):
        self.__ingredientesSeleccionados = value

    def getAdiciones(self):
        return self.__adiciones

    def setAdiciones(self, value):
        self.__adiciones = value

    def getAdicionesSeleccionadas(self):
        return self.__adicionesSeleccionadas

    def setAdicionesSeleccionadas(self, value):
        self.__adicionesSeleccionadas = value

    def getMaxIngBase(self):
        return self.__maxIngBase

    def setMaxIngBase(self, value):
        self.__maxIngBase = value

    def getaAlicaMax(self):
        return self.__aplicaMax

    def setaAlicaMax(self, value):
        self.__aplicaMax = value

    def getMinIngBase(self):
        return self.__minIngBase

    def setMinIngBase(self, value):
        self.__minIngBase = value

    def getAplicaMin(self):
        return self.__aplicaMin

    def setAplicaMin(self, value):
        self.__aplicaMin = value

