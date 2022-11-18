from app.objetos_sesion.Producto import Producto

class Bebida(Producto):
    
    def __init__(self, idProducto="", nombre="", precio=0, foto="", ingredientes=[], ingredientesSeleccionados=[], adiciones=[], adicionesSeleccionadas=[], maxIngBase="", aplicaMax="", minIngBase="", aplicaMin=""):
        super().__init__(idProducto, nombre, precio, foto, 3, ingredientes, ingredientesSeleccionados, adiciones, adicionesSeleccionadas, maxIngBase, aplicaMax, minIngBase, aplicaMin)




