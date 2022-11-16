class Carrito:

    def __init__(self, idCarrito,subTotal, itemsCarrito, cliente, fechaFinalizacion, estado):
        self.__idCarrito = idCarrito
        self.__subTotal = subTotal
        self.__itemsCarrito = itemsCarrito
        self.__cliente = cliente
        self.__fechaFinalizacion = fechaFinalizacion
        self.__estado = estado


    def calcularValor(self):
        precioCarrito = 0
        for itemCarrito in self.__itemsCarrito:
            productos = itemCarrito.getProductos()
            menu = itemCarrito.getMenu() 
            #Verifica si los productos cargados en el carrito son exactamente los del menu, si no carga los precios por producto, si son los del menu carga el precio del menu
            productosMenu = []
            entrada = menu.getEntrada()
            bebida = menu.getBebida()
            postre = menu.getPostre()
            platoFuerte = menu.getPlatoFuerte()
            acompanamiento = menu.getAcompanamiento()

            if entrada is not None:
                productosMenu.append(entrada)
            if bebida is not None:
                productosMenu.append(bebida)
            if postre is not None:
                productosMenu.append(postre)
            if platoFuerte is not None:
                productosMenu.append(platoFuerte)
            if acompanamiento is not None:
                productosMenu.append(acompanamiento)

            precioPorProducto = 0
            precioPorMenuBasico = menu.getPrecio()
            cuentaMismosProductos = 0
            for producto in productos:
                for productoMenu in productosMenu:
                    if productoMenu.getIdProducto() == producto.getIdProducto():
                        cuentaMismosProductos += 1
                precioPorProducto += producto.getPrecio()

            precioItem = precioPorProducto
            if cuentaMismosProductos == len(productos) and cuentaMismosProductos == len(productosMenu):
                precioItem = precioPorMenuBasico

            print("precio item ", precioItem)
            precioAdiciones = 0
            for producto in productos:
                adiciones = producto.getAdicionesSeleccionadas()
                for adicion in adiciones:
                    precioAdiciones += adicion.getPrecio()

            precioItem += precioAdiciones

            print("precio adicion ", precioAdiciones)
            precioCarrito += precioItem

        return precioCarrito

