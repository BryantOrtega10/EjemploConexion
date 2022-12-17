import os

from werkzeug.utils import secure_filename

from app.datos.IngredienteModelo import IngredienteModelo


class IngredienteControlador:

    def __init__(self):
        self.__modelo = IngredienteModelo()
        self.__UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname( __file__ ), "../..", 'static/uploads'))

    def lista(self):
        ingredientes = self.__modelo.obtener()
        return ingredientes

    def obtener_x_id(self, id):
        ingrediente = self.__modelo.obtenerUno(id)
        return ingrediente

    def agregar(self, request):
        foto = ''
        if 'foto' in request.files:
            file = request.files['foto']
            if file.filename != '':
                foto = secure_filename(file.filename)
                file.save(os.path.join(self.__UPLOAD_FOLDER, foto))
        
        res = self.__modelo.agregar(request.form.get('nombre'), foto, request.form.get('und_medida'))
        return res

    def modificar(self, id, request):
        ingrediente = self.__modelo.obtenerUno(id)
        ingrediente = ingrediente[0]

        foto = ingrediente["foto"]
        if 'foto' in request.files:
            file = request.files['foto']
            if file.filename != '':
                os.remove(self.__UPLOAD_FOLDER + "/" + foto)
                foto = secure_filename(file.filename)
                file.save(os.path.join(self.__UPLOAD_FOLDER, foto))
        

        res = self.__modelo.modificar(request.form.get('nombre'), foto, request.form.get('und_medida'), id)
        return res


    def eliminar(self, id): 
        res = self.__modelo.eliminar(id)
        return res