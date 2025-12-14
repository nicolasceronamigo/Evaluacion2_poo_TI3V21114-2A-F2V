from clases.producto_digital import ProductoDigital

class LicenciaSoftware(ProductoDigital):
    def __init__(self, codigo: int, nombre: str, precio_un: float, tipo_licencia: str, detalle_licencia: str):
        super().__init__(codigo, nombre, precio_un, tipo_licencia)
        self.__detalle_licencia = detalle_licencia