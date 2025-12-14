from clases.tienda import Tienda
from clases.compra_producto import CompraProducto

class Carrito:
    def __init__(self, id_cliente: str):
        self.__id_cliente = id_cliente
        self.__dicc_compra_productos = {}
    
    def producto_existe(self, codigo_producto):
        key_producto = str(codigo_producto)
        if key_producto in self.__dicc_compra_productos.keys():
            return True
        return False

    def agregar(self, tienda: Tienda, codigo_producto: int, cantidad: int):
        if tienda.producto_existe(codigo_producto):
            tienda.quitar_producto(codigo_producto, cantidad)
            producto_tienda = tienda.get_producto(codigo_producto)
            key_producto = str(codigo_producto)
            if self.producto_existe(codigo_producto):# si el producto ya está agregado en el carrito, sumar la cantidad
                self.__dicc_compra_productos[key_producto].agregar_unidades(cantidad)
                return f"{cantidad} unidad/es de {producto_tienda.get_nombre()} agregada al carrito cliente {self.__id_cliente}: \n {self.__dicc_compra_productos[key_producto].mostrar_compra_producto()}"
            compra = CompraProducto(producto_tienda, cantidad)
            self.__dicc_compra_productos[key_producto] = compra
            return f"Compra agregada al carrito cliente {self.__id_cliente}: \n {self.__dicc_compra_productos[key_producto].mostrar_compra_producto()}"
        
    def eliminar(self, codigo_producto: int):
        key_producto = str(codigo_producto)
        if self.producto_existe(codigo_producto):
            self.__dicc_compra_productos.pop(key_producto)
            return f"Producto codigo {codigo_producto} eliminado del carrito cliente {self.__id_cliente}"
        return f"Producto codigo {codigo_producto} no existe en carrito cliente {self.__id_cliente}"
    
    def mostrar_carrito(self):
        carrito = f"Carrito cliente {self.__id_cliente} \n \n"
        for compra_producto in self.__dicc_compra_productos.values():
            carrito += compra_producto.mostrar_compra_producto() + "\n"
        return carrito
    
    def total_carrito(self):
        total = 0
        for compra in self.__dicc_compra_productos.values():
            total += compra.calcular_total()
        return f"Total carrito cliente {self.__id_cliente}: {total}"