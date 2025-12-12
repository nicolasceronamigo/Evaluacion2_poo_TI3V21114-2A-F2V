from clases.vehiculo import Vehiculo, peso_persona

class VehiculoCarga(Vehiculo):
    def __init__(self, cap_carga: float, **kwargs):
        super().__init__(**kwargs)
        self.__cap_carga = cap_carga
    
    #El método toma en cuenta la capacidad de carga
    def calc_carga_total(self) -> float:
        #self.__cap_carga / 2 se asume como la carga promedio y se suma el peso del conductor
        peso_total = peso_persona + self.__cap_carga / 2
        return peso_total
    
    def calc_consumo_km_real(self): #litros de combustible por km recorrido con carga
        consumo_km_real = self.calc_consumo_km_nominal() + self.calc_carga_total() * self.calc_factor_peso()
        return consumo_km_real
    
    def calc_consumo(self, kilometros: float) -> float: #litros de combustible
        return self.calc_consumo_km_real() * kilometros