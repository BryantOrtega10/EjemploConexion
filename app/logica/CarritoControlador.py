import os
from app.datos.CarritoModelo import CarritoModelo
from werkzeug.utils import secure_filename


class CarritoControlador:

    def __init__(self):
        self.__modelo = CarritoModelo()
        self.__UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", 'static/uploads'))

    def lista(self):
        carritos = self.__modelo.obtener()
        return carritos

    def obtener_x_id(self, id):
        carrito = self.__modelo.obtenerUno(id)
        return carrito

    def agregar(self, request):
        res = self.__modelo.agregar(request.form.get('sub_total'), request.form.get('fecha_creacion'), request.form.get('fecha_finalizacion'), request.form.get('estado'), request.form.get('id_cliente'))
        return res

    def modificar(self, id, request):
        res = self.__modelo.modificar(id, request.form.get('sub_total'), request.form.get('fecha_creacion'), request.form.get('fecha_finalizacion'), request.form.get('estado'), request.form.get('id_cliente'))
        return res

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res