from clases.producto import Producto

class ProductoFisico(Producto):
    def __init__(self, codigo: int, nombre: str, precio_un: float, stock: int, peso: float):
        super().__init__(codigo, nombre, precio_un)
        self.__stock = stock
        self.__peso = peso
    
    def get_tamaño(self):
        return 0

    def get_licencia(self):
        return None

    def get_peso(self):
        return self.__peso

    def get_stock(self):
        return self.__stock

    def set_stock(self, stock: int):
        self.__stock = stock

    def agregar_stock(self, cantidad):
        if cantidad > 0:
            self.__stock += cantidad
            return f"Se agregaron {cantidad} unidades de {self.get_codigo()}. Nuevo stock: {self.__stock}"
        return f"La cantidad tiene que ser positiva"

    def quitar_stock(self, cantidad):
        if cantidad > 0:
            if self.__stock < cantidad:
                return f"Error quitar. No hay stock para la cantidad solicitada: {cantidad}"
            self.__stock -= cantidad
            return f"Se quitó {cantidad} unidad/es, de {self.get_codigo()}"
        return f"Error quitar. Cantidad {cantidad} debe ser positiva"