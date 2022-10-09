from ast import In
from app.datos.IngredienteModelo import Ingrediente

ingrediente = Ingrediente()
ingrediente.agregar_ingrediente("Carne Res","rutaFoto", "Kg")
ingrediente.agregar_ingrediente("Carne Pollo","rutaFoto", "Kg")
ingrediente.agregar_ingrediente("Carne Cerdo","rutaFoto", "Kg")
print(ingrediente.obtener_ingredientes(10))
