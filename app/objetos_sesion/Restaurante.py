from app.logica.RestauranteControlador import RestauranteControlador


class Restaurante:
    def __init__(self, id_restaurante='', nombre='', logo='', en_servicio='', especialidad='', sedes=[], horarios=[], productos=[], menus=[]):
        self.__id = id_restaurante
        self.__nombre = nombre
        self.__logo = logo
        self.__en_servicio = en_servicio
        self.__especialidad = especialidad
        self.__sedes = sedes
        self.__horarios = horarios
        self.__productos = productos
        self.__menus = menus

        self.__restauranteControlador = RestauranteControlador()

    def getId(self):
        return self.__id

    def setId(self, value):
        self.__id = value

    def getNombre(self):
        return self.__nombre

    def setNombre(self, value):
        self.__nombre = value

    def getLogo(self):
        return self.__logo

    def setLogo(self, value):
        self.__logo = value

    def getEnServicio(self):
        return self.__en_servicio

    def setEnServicio(self, value):
        self.__en_servicio = value

    def getEspecialidad(self):
        return self.__especialidad

    def setEspecialidad(self, value):
        self.__especialidad = value

    def getSedes(self):
        return self.__sedes

    def setSedes(self, value):
        self.__sedes = value

    def getHorarios(self):
        return self.__horarios

    def setHorarios(self, value):
        self.__horarios = value

    def getProductos(self):
        return self.__productos

    def setProductos(self, value):
        self.__productos = value

    def getMenus(self):
        return self.__menus

    def setMenus(self, value):
        self.__menus = value



