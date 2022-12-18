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

    def agregar(self, request):
        foto = ''
        if 'foto' in request.files:
            file = request.files['foto']
            if file.filename != '':
                foto = secure_filename(file.filename)
                file.save(os.path.join(self.__UPLOAD_FOLDER, foto))

        tipoProducto = ['Entrada ', 'Plato Fuerte', 'Postre', 'Bebida', 'Acompañamiento']
        tipoProducto = tipoProducto.index(request.form.get('tipo'))
        if request.form.get('aplica_maximo'):
            aplica_maximo = 1
        else:
            aplica_maximo = 0
        if request.form.get('aplica_minimo'):
            aplica_minimo = 1
        else:
            aplica_minimo = 0
        res = self.__modelo.agregar(nombre=request.form.get('nombre'), precio=int(request.form.get('precio')), tipo=tipoProducto,
                                    foto=foto, maximo_ingredientes_base=int(request.form.get('maximo_ingredientes_base')),
                                    aplica_maximo=aplica_maximo, minimo_ingredientes_base=int(request.form.get('minimo_ingredientes_base')),
                                    aplica_minimo=aplica_minimo, id_restaurante=int(request.form.get('id_restaurante')))
        if res['success']:
            id_producto = res['row_id']
            adicion_modelo = ProductoAdicionModelo()
            producto_ingrediente_base_modelo = ProductoIngredienteBaseModelo()
            for i in range(len(request.form.getlist('adiciones[]'))):
                res = adicion_modelo.agregar(id_producto=id_producto, id_adicion=int(request.form.get(f'id_adicion{i}')),
                                             precio=int(request.form.get(f'precio{i}')))
                if not res['success']:
                    break
            if res['success']:
                for i in range(len(request.form.getlist('ingresBase[]'))):
                    if request.form.get(f'auto_select{i}'):
                        auto_select = 1
                    else:
                        auto_select = 0
                    res = producto_ingrediente_base_modelo.agregar(id_producto=id_producto,
                                                                   id_ingrediente_base=int(request.form.get(f'id_ingrediente_base{i}')),
                                                                   auto_select=auto_select)
                    if not res['success']:
                        break
            res['row_id'] = id_producto

        return res

    # para probar con un diccionario que ejecute bien
    def tempAgregar(self, request):
        res = self.__modelo.agregar(request['nombre'], request['precio'], request['tipo'],
                                    request['foto'], request['maximo_ingredientes_base'],
                                    request['aplica_maximo'], request['minimo_ingredientes_base'],
                                    request['aplica_minimo'], request['id_restaurante'])

        if res['success']:
            id_producto = res['row_id']
            adicion_modelo = ProductoAdicionModelo()
            producto_ingrediente_base_modelo = ProductoIngredienteBaseModelo()
            for adicion in request['adiciones']:
                res = adicion_modelo.agregar(id_producto=id_producto, id_adicion=adicion['id_adicion'], precio=adicion['precio'])

            for ingrediente_base in request['ingredientes_base']:
                res = producto_ingrediente_base_modelo.agregar(id_producto=id_producto,
                                                               id_ingrediente_base=ingrediente_base['id_ingrediente_base'],
                                                               auto_select=ingrediente_base['auto_select'])
            res['row_id'] = id_producto
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
        producto_ingrediente_base_modelo = ProductoIngredienteBaseModelo()
        producto_adicion_modelo = ProductoAdicionModelo()

        res = producto_ingrediente_base_modelo.eliminarPorProducto(id_producto=id)
        if res['success']:
            res = producto_adicion_modelo.eliminarPorProducto(id_producto=id)
        if res['success']:
            res = self.__modelo.eliminar(id)
        return res

    # Trae la informacion para relacionar al producto con sus ingredientes
    def obtener_info_producto_ingredientes_base(self, id_producto):
        respuesta = []
        producto_ingrediente_base_modelo = ProductoIngredienteBaseModelo()

        infoTabla = producto_ingrediente_base_modelo.obtenerFKIngredientesBase(id_producto)
        for row in infoTabla:
            producto_ingrediente_base = dict(id_ingrediente_base=row['fk_ingrediente_base'],
                                             auto_select=row["auto_select"])
            respuesta.append(producto_ingrediente_base)

        return respuesta

    # Trae la informacion para relacionar al producto con sus adiciones
    def obtener_info_producto_adiciones(self, id_producto):
        respuesta = []
        producto_adicion_modelo = ProductoAdicionModelo()

        infoTabla = producto_adicion_modelo.obtenerFKAdiciones(id_producto)
        if infoTabla:
            for row in infoTabla:
                producto_adicion = dict(id_adicion=row['fk_adicion'],
                                        precio=row['precio'])
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
