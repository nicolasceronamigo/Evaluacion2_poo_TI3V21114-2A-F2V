from clases.producto import Producto
from clases.producto_digital import ProductoDigital
from clases.producto_fisico import ProductoFisico
from clases.tienda import Tienda
from clases.carrito import Carrito
from clases.archivo import Archivo
from clases.curso_online import CursoOnline
from clases.licencia_software import LicenciaSoftware

tienda1 = Tienda(1)

carrito1 = Carrito(1)

p_fisico1 = ProductoFisico(1, "n_p_fisico1", 1000, 100, 0.1)
p_fisico2 = ProductoFisico(1, "n_p_fisico1", 1000, 70, 0.1)
p_fisico3 = ProductoFisico(2, "n_p_fisico2", 2000, 20, 20)
p_fisico4 = ProductoFisico(3, "n_p_fisico3", 3000, 30, 30)

p_archivo1 = Archivo(4, "nom_archivo1", 10000, "licencia2", 500)
p_curso1 = CursoOnline(5, "nom_curso1", 15000, "licencia1", "certificacion1")
p_software1 = LicenciaSoftware(6, "nom_software1", 20000, "licencia3", "detalle_licencia1")

print("--------------------------------------------------------------------------------------------------\n")

print(tienda1.agregar_producto_fisico(p_fisico1))
print(tienda1.agregar_producto_fisico(p_fisico2))
print(tienda1.agregar_producto_fisico(p_fisico3))
print(tienda1.agregar_producto_fisico(p_fisico4))

print("--------------------------------------------------------------------------------------------------\n")

print(tienda1.agregar_producto_digital(p_archivo1))
print(tienda1.agregar_producto_digital(p_curso1))
print(tienda1.agregar_producto_digital(p_software1))


print("--------------------------------------------------------------------------------------------------\n")

print(tienda1.catalogo_productos())

print("--------------------------------------------------------------------------------------------------\n")

print(carrito1.agregar(tienda1, p_fisico1.get_codigo(), 4))
print(carrito1.agregar(tienda1, p_fisico2.get_codigo(), 4))
print(carrito1.agregar(tienda1, p_fisico3.get_codigo(), 4))
print(carrito1.agregar(tienda1, p_fisico4.get_codigo(), 4))
print(carrito1.agregar(tienda1, p_archivo1.get_codigo(), 4))
print(carrito1.agregar(tienda1, p_curso1.get_codigo(), 4))
print(carrito1.agregar(tienda1, p_software1.get_codigo(), 4))

print("--------------------------------------------------------------------------------------------------\n")

print(carrito1.mostrar_carrito())

print("--------------------------------------------------------------------------------------------------\n")

print(carrito1.total_carrito())

print("--------------------------------------------------------------------------------------------------\n")

print(carrito1.eliminar(1))

print("--------------------------------------------------------------------------------------------------\n")

print(carrito1.mostrar_carrito())

print("--------------------------------------------------------------------------------------------------\n")

print(carrito1.total_carrito())

print("--------------------------------------------------------------------------------------------------\n")