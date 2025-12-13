from clases.trabajador import Trabajador
from clases.gerente import Gerente
from clases.honorario import Honorario, valor_hora
from clases.vendedor import Vendedor

from clases.empresa import Empresa

empresa1 = Empresa()

print("----------------------------------------------------------------------------------------------------------------\n")

print(empresa1.agregar_trabajador("Honorario", "nombre_hon1", "rut_hon1", 100000, "Activo", 100))
print(empresa1.agregar_trabajador("Honorario", "nombre_hon2", "rut_hon2", 110000, "Activo", 110))
print(empresa1.agregar_trabajador("Honorario", "nombre_hon3", "rut_hon3", 120000, "Inactivo", 120))

honorario4 = Honorario("nombre_hon4", "rut_hon4", 130000, "Activo", 130)
print(empresa1.incorporar_trabajador(honorario4))

print(empresa1.agregar_trabajador("Vendedor", "nombre_ven1", "rut_ven1", 500000, "Activo", 1000000))
print(empresa1.agregar_trabajador("Vendedor", "nombre_ven2", "rut_ven2", 550000, "Activo", 1100000))
print(empresa1.agregar_trabajador("Vendedor", "nombre_ven3", "rut_ven3", 600000, "Inactivo", 1200000))

vendedor4 = Vendedor("nombre_ven4", "rut_ven4", 650000, "Activo", 1300000)
print(empresa1.incorporar_trabajador(vendedor4))

print(empresa1.agregar_trabajador("Gerente", "nombre_ger1", "rut_ger1", 1000000, "Activo", 200000))
print(empresa1.agregar_trabajador("Gerente", "nombre_ger2", "rut_ger2", 1100000, "Activo", 210000))
print(empresa1.agregar_trabajador("Gerente", "nombre_ger3", "rut_ger3", 1200000, "Inactivo", 220000))

gerente4 = Gerente("nombre_ger4", "rut_ger4", 1300000, "Activo", 230000)
print(empresa1.incorporar_trabajador(gerente4))

print("----------------------------------------------------------------------------------------------------------------\n")

print(empresa1.listar_activos())

print("----------------------------------------------------------------------------------------------------------------\n")

print(empresa1.listar_todos())

print("----------------------------------------------------------------------------------------------------------------\n")

print(empresa1.lista_mayor_salario())

print("----------------------------------------------------------------------------------------------------------------\n")

print(empresa1.reporte())

print("----------------------------------------------------------------------------------------------------------------\n")