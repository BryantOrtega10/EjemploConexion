from app.datos.UsuarioModelo import UsuarioModelo

class UsuarioControlador:

    def __init__(self):
        self.__modelo = UsuarioModelo()

    def lista(self):
        usuarios = self.__modelo.obtener()
        return usuarios

    def obtener_x_id(self, id):
        usuario = self.__modelo.obtenerUno(id)
        return usuario

    def agregar(self):
        pass

    def modificar(self):
        pass

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res