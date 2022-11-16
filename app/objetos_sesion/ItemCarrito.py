class ItemCarrito:
    def __init__(self, idItemCarrito, menu, sede, productos):
        self.__idItemCarrito = idItemCarrito
        self.__menu = menu
        self.__sede = sede
        self.__productos = productos

    def getProductos(self):
        return self.__productos

    def getMenu(self):
        return self.__menu