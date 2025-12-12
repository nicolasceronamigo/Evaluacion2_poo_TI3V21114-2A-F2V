from clases.vehiculo import peso_persona
from clases.vehiculo_pasajero import VehiculoPasajero
from clases.vehiculo_carga import VehiculoCarga

class Bus(VehiculoPasajero, VehiculoCarga):
    #transporta carga y pasajeros
    def __init__(self, patente: str, marca: str, modelo: str, año_fabricacion: int, cilindrada: float, 
                rendimiento_nominal: float, cap_pasajeros: int, cap_carga: float, peso: float):
        super().__init__(patente = patente, marca = marca, modelo = modelo,año_fabricacion = año_fabricacion, 
                        cilindrada = cilindrada, rendimiento_nominal = rendimiento_nominal, 
                        cap_pasajeros = cap_pasajeros, cap_carga = cap_carga, peso = peso)
    
    def calc_carga_total(self) -> float:
        suma_cargas = VehiculoPasajero.calc_carga_total(self) + VehiculoCarga.calc_carga_total(self)
        return suma_cargas - peso_persona #peso_persona se repite 2 veces, asi que se resta una vez