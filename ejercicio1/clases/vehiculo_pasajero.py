from clases.vehiculo import Vehiculo, peso_persona

class VehiculoPasajero(Vehiculo):
    def __init__(self, cap_pasajeros: int, **kwargs):
        super().__init__(**kwargs)
        self.__cap_pasajeros = cap_pasajeros
    
    #El método toma en cuenta la capacidad de pasajeros
    def calc_carga_total(self) -> float:
        #self.__cap_carga / 2 se asume como la carga promedio y self.__cap_pasajeros / 2 se asume como los pasajeros promedio
        carga_total = peso_persona + peso_persona * self.__cap_pasajeros / 2 #el primer peso_persona sería el conductor
        return carga_total
    
    def calc_consumo_km_real(self): #litros de combustible por km recorrido con pasajeros
        consumo_km_real = self.calc_consumo_km_nominal() + self.calc_carga_total() * self.calc_factor_peso()
        return consumo_km_real
    
    def calc_consumo(self, kilometros: float) -> float:
        return self.calc_consumo_km_real() * kilometros