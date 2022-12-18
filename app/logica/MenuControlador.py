import os

from werkzeug.utils import secure_filename

from app.datos.MenuModelo import MenuModelo
from app.datos.MenuProductoModelo import MenuProductoModelo
from app.datos.ProductoModelo import ProductoModelo


class MenuControlador:

    def __init__(self):
        self.__modelo = MenuModelo()
        self.__UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", 'static/uploads'))

    def lista(self):
        menus = self.__modelo.obtener()
        return menus
    
    def lista_por_restaurante(self, id_rest):
        menus = self.__modelo.obtener_x_rest(id_rest)
        return menus

    def obtener_x_id(self, id):
        respuesta = {}
        menu = self.__modelo.obtenerUno(id)
        if menu:
            respuesta['menu'] = menu[0]
            respuesta['productos'] = self.obtener_info_menu_productos(id)
            respuesta['entrada'] = None
            respuesta['platoFuerte'] = None
            respuesta['bebida'] = None
            respuesta['postre'] = None
            respuesta['acompanamiento'] = None

        return respuesta

    def agregar(self, request):
        foto = ''
        if 'foto' in request.files:
            file = request.files['foto']
            if file.filename != '':
                foto = secure_filename(file.filename)
                file.save(os.path.join(self.__UPLOAD_FOLDER, foto))

        res = self.__modelo.agregar(request.form.get('nombre'), foto, request.form.get('precio'), request.form.get('id_restaurante'))
        return res

    def modificar(self, id, request):
        menu = self.__modelo.obtenerUno(id)
        menu = menu[0]

        foto = menu["foto"]
        if 'foto' in request.files:
            file = request.files['foto']
            if file.filename != '':
                os.remove(self.__UPLOAD_FOLDER + "/" + foto)
                foto = secure_filename(file.filename)
                file.save(os.path.join(self.__UPLOAD_FOLDER, foto))

        res = self.__modelo.modificar(id, request.form.get('nombre'), foto, request.form.get('und_medida'), request.form.get('id_restaurante'))
        return res

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res

    def obtener_info_menu_productos(self, id_menu):
        menu_producto_modelo = MenuProductoModelo()

        return menu_producto_modelo.obtenerFKProductos(id_menu)
