from app.datos.AdicionModelo import AdicionModelo


class AdicionControlador:

    def __init__(self):
        self.__modelo = AdicionModelo()

    def lista(self):
        adiciones = self.__modelo.obtener()
        return adiciones

    def obtener_x_id(self, id):
        adicion = self.__modelo.obtenerUno(id)
        return adicion

    def agregar(self, request):
        res = self.__modelo.agregar(request.form.get('id_ingrediente'), request.form.get('cantidad'), request.form.get('maximo'))
        return res

    def modificar(self, id, request):
        res = self.__modelo.modificar(id, request.form.get('id_ingrediente'), request.form.get('cantidad'), request.form.get('maximo'))
        return res

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res