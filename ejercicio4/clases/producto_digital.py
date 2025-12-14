from clases.producto import Producto

class ProductoDigital(Producto):
    def __init__(self, codigo: int, nombre: str, precio_un: float, tipo_licencia: str):
        super().__init__(codigo, nombre, precio_un)
        self.__tipo_licencia = tipo_licencia
    
    def get_peso(self):
        return 0
    
    def get_licencia(self):
        return self.__tipo_licencia
    
    def get_tamaño(self):
        return 0

    def quitar_stock(self, cantidad):
        '''Solo se verifica que la cantidad solicitada sea positiva'''
        if cantidad > 0:
            return f"Se quitó {cantidad} unidad/es, de {self.get_codigo()}"
        return f"Error quitar. Cantidad {cantidad} debe ser positiva"