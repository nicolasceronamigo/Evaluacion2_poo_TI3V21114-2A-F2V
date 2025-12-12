peso_persona: float = 70 #peso de un pasajero promedio, en kg

class Vehiculo:
    def __init__(self, patente: str, marca: str, modelo: str, año_fabricacion: int, cilindrada: float, rendimiento_nominal: float, peso: float):
        self.__patente = patente
        self.__marca = marca
        self.__modelo = modelo
        self.__año_fabricacion = año_fabricacion
        self.__cilindrada = cilindrada #se mide en unidades de volumen, en litros
        self.__rendimiento_nominal = rendimiento_nominal #km por litro, sin carga y sin pasajeros, se encuentra en https://consumovehicular.minenergia.cl/
        self.__peso = peso #peso del vehiculo, en kg, sin carga y sin pasajeros
    
    def calc_consumo_km_nominal(self): #litros por km sin carga ni pasajeros
        return 1 / self.__rendimiento_nominal
    
    #consumo de litros de combustible por km, por kg de peso
    def calc_factor_peso(self):
        return self.calc_consumo_km_nominal() / self.__peso
    
    def get_peso(self) -> float:
        return self.__peso
    
    def get_patente(self) -> str:
        return self.__patente
    
    def descripcion(self):
        descripcion = f"| Patente: {self.__patente} | Marca: {self.__marca} | Modelo: {self.__modelo} | Año: {self.__año_fabricacion} | Tipo: {type(self).__name__} |"
        return descripcion