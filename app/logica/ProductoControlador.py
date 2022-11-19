import os
from app.datos.ProductoModelo import ProductoModelo
from werkzeug.utils import secure_filename


class ProductoControlador:

    def __init__(self):
        self.__modelo = ProductoModelo()
        self.__UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", 'static/uploads'))

    def lista(self):
        productos = self.__modelo.obtener()
        return productos

    def obtener_x_id(self, id):
        producto = self.__modelo.obtenerUno(id)
        return producto

    def agregar(self, request):
        foto = ''
        if 'foto' in request.files:
            file = request.files['foto']
            if file.filename != '':
                foto = secure_filename(file.filename)
                file.save(os.path.join(self.__UPLOAD_FOLDER, foto))

        res = self.__modelo.agregar(request.form.get('nombre'), request.form.get('precio'), request.form.get('tipo'), request.form.get('foto'), request.form.get('maximo_ingredientes_base'), request.form.get('aplica_maximo'), request.form.get('minimo_ingredientes_base'), request.form.get('aplica_minimo'), request.form.get('id_restaurante'))
        return res

    def modificar(self, id, request):
        producto = self.__modelo.obtenerUno(id)
        producto = producto[0]

        foto = producto["foto"]
        if 'foto' in request.files:
            file = request.files['foto']
            if file.filename != '':
                os.remove(self.__UPLOAD_FOLDER + "/" + foto)
                foto = secure_filename(file.filename)
                file.save(os.path.join(self.__UPLOAD_FOLDER, foto))

        res = self.__modelo.modificar(id, request.form.get('nombre'), request.form.get('precio'), request.form.get('tipo'), request.form.get('foto'), request.form.get('maximo_ingredientes_base'), request.form.get('aplica_maximo'), request.form.get('minimo_ingredientes_base'), request.form.get('aplica_minimo'), request.form.get('id_restaurante'))
        return res

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res