import os
from app.datos.ItemCarritoModelo import ItemCarritoModelo
from werkzeug.utils import secure_filename


class ItemCarritoControlador:

    def __init__(self):
        self.__modelo = ItemCarritoModelo()
        self.__UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", 'static/uploads'))

    def lista(self):
        itemsCarrito = self.__modelo.obtener()
        return itemsCarrito

    def obtener_x_id(self, id):
        itemCarrito = self.__modelo.obtenerUno(id)
        return itemCarrito

    def agregar(self, request):
        res = self.__modelo.agregar(request.form.get('id_carrito'), request.form.get('id_menu'), request.form.get('id_sede'))
        return res

    def modificar(self, id, request):
        res = self.__modelo.modificar(id, request.form.get('id_carrito'), request.form.get('id_menu'), request.form.get('id_sede'))
        return res

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res