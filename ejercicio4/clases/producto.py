class Producto:
    def __init__(self, codigo: int, nombre: str, precio_un: float):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio_un = precio_un
        self.__tipo_producto = type(self).__name__
    
    def get_codigo(self):
        return self.__codigo
    
    def get_nombre(self):
        return self.__nombre
    
    def get_precio_un(self):
        return self.__precio_un

    def get_tipo(self):
        return self.__tipo_producto
    
    def mostrar_producto(self):
        return f"| Código: {self.__codigo} | Nombre: {self.__nombre} | Precio: {self.__precio_un} | Tipo: {self.__tipo_producto}"