from app.logica.ProductoControlador import ProductoControlador
from app.objetos_sesion.Adicion import Adicion
from app.objetos_sesion.IngredienteBase import IngredienteBase

class Producto:
    
    def __init__(self, idProducto="", nombre="", precio=0, foto="", tipoProducto="", ingredientes=[], ingredientes_base=[], ingredientesSeleccionados=[], adiciones=[], adicionesSeleccionadas=[], maxIngBase="", aplicaMax="", minIngBase="", aplicaMin="", fkRestaurante=""):
        self.__idProducto = idProducto
        self.__nombre = nombre
        self.__precio = precio
        self.__foto = foto
        self.__tipoProducto = tipoProducto
        self.__ingredientes = ingredientes
        self.__ingredientes_base = ingredientes_base
        self.__ingredientesSeleccionados = ingredientesSeleccionados
        self.__adiciones = adiciones
        self.__adicionesSeleccionadas = adicionesSeleccionadas
        self.__maxIngBase = maxIngBase
        self.__aplicaMax = aplicaMax
        self.__minIngBase = minIngBase
        self.__aplicaMin = aplicaMin
        self.__fkRestaurante = fkRestaurante

        self.__productoControlador = ProductoControlador()

    # Instancia toda la info del producto que hay en BD
    def setBdInfoProducto(self, id_producto):
        infoProducto = self.__productoControlador.obtener_x_id(id_producto)
        if infoProducto:
            producto = infoProducto['producto']
            self.__idProducto = producto['id_producto']
            self.__nombre = producto['nombre']
            self.__precio = producto['precio']
            self.__tipoProducto = producto['tipo']
            self.__foto = producto['foto']
            self.__maxIngBase = producto['maximo_ingredientes_base']
            self.__aplicaMax = producto['aplica_maximo']
            self.__minIngBase = producto['minimo_ingredientes_base']
            self.__aplicaMin = producto['aplica_minimo']
            self.__fkRestaurante = producto['fk_restaurante']

            # Se instancian todos los ingredientes que podrian componer el producto, pero no son la parte base esencial
            for ingrediente in infoProducto['ingredientes']:
                ingredienteBase = IngredienteBase()
                ingredienteBase.setBdInfoIngredienteBase(ingrediente['id_ingrediente_base'],
                                                         ingrediente['auto_select'])
                self.__ingredientes.append(ingredienteBase)

            # Se instancian todos los ingredientes que componen el producto
            for ingrediente_base in infoProducto['ingredientes_base']:
                ingredienteBase = IngredienteBase()
                ingredienteBase.setBdInfoIngredienteBase(ingrediente_base['id_ingrediente_base'],
                                                         ingrediente_base['auto_select'])
                self.__ingredientes_base.append(ingredienteBase)

            # Se instancian todas las adiciones del producto
            for adicion in infoProducto['adiciones']:
                adicion_obj = Adicion()
                adicion_obj.setBdInfoAdicion(adicion['id_adicion'],
                                             adicion['precio'])
                self.__adiciones.append(adicion_obj)



    # Obtiene todos los ingredientes de cambio para un ingrediente especifico
    def getIncredientesDeCambio(self, id_ingrediente):
        return self.__productoControlador.obtener_ingredientes_cambio(id_ingrediente)

    def getIdProducto(self):
        return self.__idProducto

    def setIdProducto(self, value):
        self.__idProducto = value

    def getNombre(self):
        return self.__nombre

    def setNombre(self, value):
        self.__nombre = value

    def getPrecio(self):
        return self.__precio

    def setPrecio(self, value):
        self.__precio = value

    def getFoto(self):
        return self.__foto

    def setFoto(self, value):
        self.__foto = value

    def getTipoProducto(self):
        return self.__tipoProducto

    def setTipoProducto(self, value):
        self.__tipoProducto = value

    def getIngredientes(self):
        return self.__ingredientes

    def setIngredientes(self, value):
        self.__ingredientes = value

    def getIngredientesBase(self):
        return self.__ingredientes_base

    def setIngredientesBase(self, value):
        self.__ingredientes_base = value

    def getIngredientesSeleccionados(self):
        return self.__ingredientesSeleccionados

    def setIngredientesSeleccionados(self, value):
        self.__ingredientesSeleccionados = value

    def getAdiciones(self):
        return self.__adiciones

    def setAdiciones(self, value):
        self.__adiciones = value

    def getAdicionesSeleccionadas(self):
        return self.__adicionesSeleccionadas

    def setAdicionesSeleccionadas(self, value):
        self.__adicionesSeleccionadas = value

    def getMaxIngBase(self):
        return self.__maxIngBase

    def setMaxIngBase(self, value):
        self.__maxIngBase = value

    def getaAlicaMax(self):
        return self.__aplicaMax

    def setaAlicaMax(self, value):
        self.__aplicaMax = value

    def getMinIngBase(self):
        return self.__minIngBase

    def setMinIngBase(self, value):
        self.__minIngBase = value

    def getAplicaMin(self):
        return self.__aplicaMin

    def setAplicaMin(self, value):
        self.__aplicaMin = value

    def getFKRestaurante(self):
        return self.__fkRestaurante

    def setFKRestaurante(self, value):
        self.__fkRestaurante = value

