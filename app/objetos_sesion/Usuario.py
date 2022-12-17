from app.logica.UsuarioControlador import UsuarioControlador

class Usuario:
    def __init__(self, id_usuario='', user='', password='', rol=''):
        self.__id = id_usuario
        self.__user = user
        self.__password = password
        self.__rol = rol

    def getId(self):
        return self.__id

    def setId(self, value):
        self.__id = value

    def getUser(self):
        return self.__user

    def setUser(self, value):
        self.__user = value

    def getPassword(self):
        return self.__password

    def setPassword(self, value):
        self.__password = value

    def getRol(self):
        return self.__rol

    def setRol(self, value):
        self.__rol = value