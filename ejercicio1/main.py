from clases.automovil import Automovil
from clases.bus import Bus
from clases.camion import Camion
from clases.motocicleta import Motocicleta

from clases.flota import Flota

#Crear Autos
auto1 = Automovil(patente = "pat_auto1", marca = "marca_auto1", modelo = "mod_auto1", 
                año_fabricacion = 1991, cilindrada = 1.1, rendimiento_nominal = 15, 
                peso = 1500, cap_pasajeros = 4)

auto2 = Automovil(patente = "pat_auto2", marca = "marca_auto2", modelo = "mod_auto2", 
                año_fabricacion = 1992, cilindrada = 1.2, rendimiento_nominal = 16, 
                peso = 1600, cap_pasajeros = 5)

auto3 = Automovil(patente = "pat_auto3", marca = "marca_auto3", modelo = "mod_auto3", 
                año_fabricacion = 1993, cilindrada = 1.3, rendimiento_nominal = 17, 
                peso = 1700, cap_pasajeros = 6)

auto4 = Automovil(patente = "pat_auto4", marca = "marca_auto4", modelo = "mod_auto4", 
                año_fabricacion = 1994, cilindrada = 1.4, rendimiento_nominal = 18, 
                peso = 1800, cap_pasajeros = 7)

#Crear Buses
bus1 = Bus("pat_bus1", "marca_bus1", "mod_bus1", 2001, 11, 2.91, 41, 821, 11000)

bus2 = Bus("pat_bus2", "marca_bus2", "mod_bus2", 2002, 12, 2.92, 42, 822, 12000)

bus3 = Bus("pat_bus3", "marca_bus3", "mod_bus3", 2003, 13, 2.93, 43, 823, 13000)

#Crear camiones
camion1 = Camion(patente = "pat_camion1", marca = "marca_camion1", modelo = "mod_camion1", 
                año_fabricacion = 1981, cilindrada = 11, rendimiento_nominal = 7, 
                peso = 11000, cap_carga = 21)

camion2 = Camion(patente = "pat_camion2", marca = "marca_camion2", modelo = "mod_camion2", 
                año_fabricacion = 1982, cilindrada = 12, rendimiento_nominal = 8, 
                peso = 12000, cap_carga = 22)

#Crear motos
moto1 = Motocicleta(patente = "pat_moto1", marca = "marca_moto1", modelo = "mod_moto1", 
                año_fabricacion = 2011, cilindrada = 610, rendimiento_nominal = 21, 
                peso = 110, cap_carga = 51)

moto2 = Motocicleta(patente = "pat_moto2", marca = "marca_moto2", modelo = "mod_moto2", 
                año_fabricacion = 2012, cilindrada = 620, rendimiento_nominal = 22, 
                peso = 120, cap_carga = 52)

moto3 = Motocicleta(patente = "pat_moto3", marca = "marca_moto3", modelo = "mod_moto3", 
                año_fabricacion = 2013, cilindrada = 630, rendimiento_nominal = 23, 
                peso = 130, cap_carga = 53)

moto4 = Motocicleta(patente = "pat_moto4", marca = "marca_moto4", modelo = "mod_moto4", 
                año_fabricacion = 2014, cilindrada = 640, rendimiento_nominal = 24, 
                peso = 140, cap_carga = 54)

moto5 = Motocicleta(patente = "pat_moto5", marca = "marca_moto5", modelo = "mod_moto5", 
                año_fabricacion = 2015, cilindrada = 650, rendimiento_nominal = 25, 
                peso = 150, cap_carga = 55)

#Crear lista de vehiculos
lista_flota = [auto1, auto2, auto3, auto4, bus1, bus2, bus3, 
            camion1, camion2, moto1, moto2, moto3, moto4, moto5]

#Crear flota
flota1 = Flota()

#agregar vehiculos a la flota
for vehiculo in lista_flota:
    print(flota1.agregar_vehiculo(vehiculo))

print("--------------------------------------------------------------------------------------------------------\n")

#eliminar auto1 "pat_auoto1"
print(flota1.eliminar_vehiculo("pat_auto1"))

print("--------------------------------------------------------------------------------------------------------\n")

#buscar auto1 "pat_auoto1"
print(flota1.consultar_vehiculo("pat_auto1"))

print("--------------------------------------------------------------------------------------------------------\n")

#agregar auto1 "pat_auoto1"
print(flota1.agregar_vehiculo(auto1))

print("--------------------------------------------------------------------------------------------------------\n")

#buscar auto1 "pat_auoto1"
print(flota1.consultar_vehiculo("pat_auto1"))

print("--------------------------------------------------------------------------------------------------------\n")


#Mostrar todos los vahiculos
print(flota1.mostrar_vehiculos())

print("--------------------------------------------------------------------------------------------------------\n")

#Mostrar los consumos de todos los vehiculo en 150 km
print(flota1.listado_consumos(150))

print("--------------------------------------------------------------------------------------------------------\n")

#Mostrar la suma de todos los consumos en 150 km
print(flota1.consumo_global(150))

print("--------------------------------------------------------------------------------------------------------\n")