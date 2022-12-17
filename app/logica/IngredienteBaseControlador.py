from app.datos.IngredienteBaseModelo import IngredienteBaseModelo


class IngredienteBaseControlador:

    def __init__(self):
        self.__modelo = IngredienteBaseModelo()

    def lista(self):
        ingredientesBase = self.__modelo.obtener()
        return ingredientesBase

    def obtener_x_id(self, id):
        ingredienteBase = self.__modelo.obtenerUno(id)
        return ingredienteBase

    def agregar(self, request):
        res = self.__modelo.agregar(request.form.get('cantidad'), request.form.get('id_ingrediente'))
        return res

    def modificar(self, id, request):
        res = self.__modelo.modificar(id, request.form.get('cantidad'), request.form.get('id_ingrediente'))
        return res

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res