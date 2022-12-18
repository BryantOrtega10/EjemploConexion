import os

from werkzeug.utils import secure_filename

from app.datos.AdicionModelo import AdicionModelo
from app.datos.IngredienteBaseModelo import IngredienteBaseModelo
from app.datos.IngredienteCambioModelo import IngredienteCambioModelo
from app.datos.IngredienteModelo import IngredienteModelo
from app.datos.ProductoAdicionModelo import ProductoAdicionModelo
from app.datos.ProductoIngreBaseModelo import ProductoIngredienteBaseModelo
from app.datos.ProductoModelo import ProductoModelo


class ProductoControlador:

    def __init__(self):
        self.__modelo = ProductoModelo()
        self.__UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), "../..", 'static/uploads'))

    def lista(self):
        productos = self.__modelo.obtener()
        return productos

    # Trae toda la informacion del producto y la de sus relaciones en las diferentes tablas
    def obtener_x_id(self, id):
        respuesta = {}
        ingredientes = []
        producto = self.__modelo.obtenerUno(id)
        if producto:
            respuesta["producto"] = producto[0]
            ingredientes_base = self.obtener_info_producto_ingredientes_base(id)
            for i, ingrediente_base in enumerate(ingredientes_base):
                if not ingrediente_base["auto_select"]:
                    ingredientes.append(ingrediente_base.pop(i))
            respuesta["ingredientes_base"] = ingredientes_base
            respuesta["ingredientes"] = ingredientes
            respuesta["adiciones"] = self.obtener_info_producto_adiciones(id)
        return respuesta
       
    def lista_por_restaurante(self, id_rest):
        productos = self.__modelo.obtener_x_rest(id_rest)
        return productos

    def agregar(self, request):
        foto = ''
        if 'foto' in request.files:
            file = request.files['foto']
            if file.filename != '':
                foto = secure_filename(file.filename)
                file.save(os.path.join(self.__UPLOAD_FOLDER, foto))

        res = self.__modelo.agregar(request.form.get('nombre'), request.form.get('precio'), request.form.get('tipo'),
                                    request.form.get('foto'), request.form.get('maximo_ingredientes_base'),
                                    request.form.get('aplica_maximo'), request.form.get('minimo_ingredientes_base'),
                                    request.form.get('aplica_minimo'), request.form.get('id_restaurante'))
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

        res = self.__modelo.modificar(id, request.form.get('nombre'), request.form.get('precio'),
                                      request.form.get('tipo'), request.form.get('foto'),
                                      request.form.get('maximo_ingredientes_base'), request.form.get('aplica_maximo'),
                                      request.form.get('minimo_ingredientes_base'), request.form.get('aplica_minimo'),
                                      request.form.get('id_restaurante'))
        return res

    def eliminar(self, id):
        res = self.__modelo.eliminar(id)
        return res

    # Trae la informacion para relacionar al producto con sus ingredientes
    def obtener_info_producto_ingredientes_base(self, id_producto):
        respuesta = []
        producto_ingrediente_base_modelo = ProductoIngredienteBaseModelo()

        infoTabla = producto_ingrediente_base_modelo.obtenerFKIngredientesBase(id_producto)
        for row in infoTabla:
            producto_ingrediente_base = dict(id_ingrediente_base=row['fk_ingrediente_base'],
                                             auto_select=row["auto_select"],
                                             cantidad=row["cantidad"],
                                             id_ingrediente=row["id_ingrediente"],
                                             nombre=row['nombre'],
                                             und_medida=row['und_medida'],
                                             foto=row['foto'])
            respuesta.append(producto_ingrediente_base)

        return respuesta

    # Trae la informacion para relacionar al producto con sus adiciones
    def obtener_info_producto_adiciones(self, id_producto):
        respuesta = []
        producto_adicion_modelo = ProductoAdicionModelo()
        adicion_modelo = AdicionModelo()
        ingrediente_modelo = IngredienteModelo()

        infoTabla = producto_adicion_modelo.obtenerFKAdiciones(id_producto)
        if infoTabla:
            for row in infoTabla:
                producto_adicion = dict(id_adicion=row['fk_adicion'],
                                        precio=row['precio'],
                                        maximo=row["maximo"],
                                        id_ingrediente=row["id_ingrediente"],
                                        nombre=row['nombre'],
                                        und_medida=row['und_medida'],
                                        foto=row['foto'])
                respuesta.append(producto_adicion)

        return respuesta

    def obtener_ingredientes_cambio(self, id_ingrediente):
        respuesta = []
        ingrediente_cambio_modelo = IngredienteCambioModelo()
        inrediente_base_modelo = IngredienteBaseModelo()
        ingrediente_modelo = IngredienteModelo()
        infoTabla = ingrediente_cambio_modelo.obtenerFKIngredientesDeCambio(id_ingrediente)
        for row in infoTabla:
            resTemp = inrediente_base_modelo.obtenerUno(row["fk_ingrediente_cambio"])[0]
            ingrediente_cambio = dict(id_ingrediente_base=resTemp["id_ingrediente_base"],
                                    cantidad=resTemp["cantidad"])
            resTemp = ingrediente_modelo.obtenerUno(resTemp['fk_ingrediente'])[0]
            for key, value in resTemp.items():
                ingrediente_cambio[key] = value
            respuesta.append(ingrediente_cambio)

        return respuesta
