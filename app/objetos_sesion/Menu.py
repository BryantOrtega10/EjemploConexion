class Menu:

    def __init__(self, idMenu, nombre, foto, precio, estado, entrada, bebida, postre, platoFuerte, acompanamiento):
        self.__idMenu = idMenu
        self.__nombre = nombre
        self.__foto = foto
        self.__precio = precio
        self.__estado = estado
        self.__entrada = entrada
        self.__bebida = bebida
        self.__postre = postre
        self.__platoFuerte = platoFuerte
        self.__acompanamiento = acompanamiento

    def getEntrada(self):
        return self.__entrada
    
    def getBebida(self):
        return self.__bebida

    def getPostre(self):
        return self.__postre

    def getPlatoFuerte(self):
        return self.__platoFuerte
    
    def getAcompanamiento(self):
        return self.__acompanamiento

    def getPrecio(self):
        return self.__precio