
from app.datos.MysqlConnector import MysqlConnection

class Ingrediente:

    def __init__(self):
        self.__conector = MysqlConnection()

    def agregar_ingrediente(self, nombre, foto, unidad_medida):
        #Validaciones        
        res = self.__conector.insert("ingrediente", {"nombre": nombre, "foto": foto, "unidad_medida": unidad_medida})
        return (res == 1)
    
    def obtener_ingredientes(self, limite):
        res = self.__conector.select(tables=["ingrediente"], limit=limite)
        return res