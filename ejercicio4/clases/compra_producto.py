from clases.producto import Producto

class CompraProducto:
    def __init__(self, producto, cantidad: int):
        self.__producto = producto
        self.__cod_producto = producto.get_codigo()
        self.__nombre = producto.get_nombre()
        self.__tipo = producto.get_tipo()
        self.__cantidad = cantidad

    def agregar_unidades(self, cantidad):
        self.__cantidad += cantidad

    def recargo_peso(self):
        peso = self.__producto.get_peso() * self.__cantidad
        if peso < 0:
            return "Error. Peso negativo."
        elif peso == 0:
            return 0
        elif peso < 10:
            return 5000
        elif peso < 50:
            return 20000
        else:
            return 50000

    def recargo_digital(self):
        licencia = self.__producto.get_licencia()
        match licencia:
            case "licencia1":
                return 0
            case "licencia2":
                return 5000
            case "licencia3":
                return 10000
            case _:
                return 0

    def recargo_archivo(self):
        tamaño = self.__producto.get_tamaño()
        if tamaño < 0:
            return "Error. Tamaño negativo."
        elif tamaño == 0:
            return 0
        elif tamaño < 1000:
            return 1000
        elif tamaño < 10000:
            return 10000
        else:
            return 50000

    def calcular_total(self):
        total_sin_rec = self.__producto.get_precio_un() * self.__cantidad
        recargos = self.recargo_peso() + (self.recargo_digital() + self.recargo_archivo()) * self.__cantidad
        total = total_sin_rec + recargos
        return total

    def mostrar_compra_producto(self):
        return f"| Nombre: {self.__nombre} | Tipo: {self.__tipo} | Cantidad: {self.__cantidad} | Total: {self.calcular_total()} |"