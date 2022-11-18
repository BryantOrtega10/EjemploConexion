class ItemCarrito:
    def __init__(self, idItemCarrito, menu, sede, productos):
        self.__idItemCarrito = idItemCarrito
        self.__menu = menu
        self.__sede = sede
        self.__productos = productos

    def getIdItemCarrito(self):
        return self.__idItemCarrito

    def setIdItemCarrito(self, value):
        self.__idItemCarrito = value

    def getMenu(self):
        return self.__menu

    def setMenu(self, value):
        self.__menu = value

    def getSede(self):
        return self.__sede

    def setSede(self, value):
        self.__sede = value

    def getProductos(self):
        return self.__productos

    def setProductos(self, value):
        self.__productos = value
