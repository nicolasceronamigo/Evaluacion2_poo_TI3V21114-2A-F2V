from clases.producto_digital import ProductoDigital

class Archivo(ProductoDigital):
    def __init__(self, codigo: int, nombre: str, precio_un: float, tipo_licencia: str, tamaño: float):
        super().__init__(codigo, nombre, precio_un, tipo_licencia)
        self.__tamaño = tamaño
    
    def get_tamaño(self):
        return self.__tamaño