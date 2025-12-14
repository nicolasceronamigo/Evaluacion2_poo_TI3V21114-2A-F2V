from clases.producto import Producto
from clases.producto_fisico import ProductoFisico
from clases.producto_digital import ProductoDigital

class Tienda:
    def __init__(self, id_tienda: int):
        self.__id_tienda = id_tienda
        self.__dicc_productos = {}
    
    def producto_existe(self, codigo_producto: int):
        key_producto = str(codigo_producto)
        if key_producto in self.__dicc_productos.keys():
            return True
        return False        

    def get_producto(self, codigo_producto):
        if self.producto_existe(codigo_producto):
            key_producto = str(codigo_producto)
            return self.__dicc_productos[key_producto]
        return None

    def agregar_producto_fisico(self, producto: ProductoFisico):
        codigo_producto = producto.get_codigo()
        key_producto = str(codigo_producto)
        if self.producto_existe(codigo_producto):
            producto_tienda = self.__dicc_productos[key_producto]
            agregar = producto_tienda.agregar_stock(producto.get_stock())
            return f"Producto {codigo_producto} ya existe en Tienda {self.__id_tienda}. " + agregar
        producto_nuevo = ProductoFisico(producto.get_codigo(), producto.get_nombre(), producto.get_precio_un(), producto.get_stock(), producto.get_peso())
        self.__dicc_productos[key_producto] = producto_nuevo
        return f"Se agrego producto {codigo_producto} a la Tienda {self.__id_tienda}"
    
    def quitar_producto(self, codigo_producto, cantidad):
        if self.producto_existe(codigo_producto):
            key_producto = str(codigo_producto)
            prod_quitar = self.__dicc_productos[key_producto]
            return prod_quitar.quitar_stock(cantidad)
        return f"Error quitar. Producto {codigo_producto} no existe en Tienda {self.__id_tienda}."
    
    def agregar_producto_digital(self, producto):
        codigo_producto = producto.get_codigo()
        key_producto = str(codigo_producto)
        if self.producto_existe(codigo_producto):
            return f"Producto {codigo_producto} ya existe en Tienda {self.__id_tienda}. "
        self.__dicc_productos[key_producto] = producto
        return f"Se agrego producto {codigo_producto} a la Tienda {self.__id_tienda}"

    def catalogo_productos(self):
        catalogo = f"Catálogo de productos tienda {self.__id_tienda} \n \n"
        for producto in self.__dicc_productos.values():
            catalogo += producto.mostrar_producto() + "\n"
        return catalogo
