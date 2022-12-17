from app.datos.AdminTecnicoModelo import AdminTecnicoModelo

class AdminTecnicoControlador:

    def __init__(self):
        self.__modelo = AdminTecnicoModelo()

    def lista(self):
        adminsTecnicos = self.__modelo.obtener()
        return adminsTecnicos

    def obtener_x_id(self, id):
        adminTecnico = self.__modelo.obtenerUno(id)
        return adminTecnico

    def agregar(self):
        pass

    def modificar(self):
        pass

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res