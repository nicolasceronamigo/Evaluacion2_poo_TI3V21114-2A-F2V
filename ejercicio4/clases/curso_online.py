from clases.producto_digital import ProductoDigital

class CursoOnline(ProductoDigital):
    def __init__(self, codigo: int, nombre: str, precio_un: float, tipo_licencia: str, certificacion: str):
        super().__init__(codigo, nombre, precio_un, tipo_licencia)
        self.__certificacion = certificacion