from clases.vehiculo import Vehiculo

class Flota:
    def __init__(self):
        self.__dicc_vehiculos: dict = {}
    
    def identificador_existe(self, identificador):
        if identificador in self.__dicc_vehiculos.keys():
            return True
        return False
    
    def agregar_vehiculo(self, vehiculo) -> str:
        identificador = vehiculo.get_patente()
        if self.identificador_existe(identificador):
            return f"Error al agregar. Patente: {identificador} ya está registrada para otro vehiculo."
        self.__dicc_vehiculos[identificador] = vehiculo
        return f"Vehiculo patente {identificador} agregado"
    
    def eliminar_vehiculo(self, identificador: str):
        if not self.identificador_existe(identificador):
            return f"Error al eliminar. Patente: {identificador} no está registrada en la flota"
        self.__dicc_vehiculos.pop(identificador)
        return f"Vehiculo patente: {identificador}, eliminado."
    
    def consultar_vehiculo(self, identificador: str) -> str:
        if not self.identificador_existe(identificador):
            return f"Error al consultar. Patente: {identificador} no está registrada en la flota"
        vehiculo = self.__dicc_vehiculos[identificador]
        return f"Búsqueda de patente {identificador}: \n" + vehiculo.descripcion()
    
    def mostrar_vehiculos(self) -> str:
        resultado = "Todos los vehiculos: \n \n"
        for vehiculo in self.__dicc_vehiculos.values():
            resultado += vehiculo.descripcion() + "\n"
        return resultado
    
    def consultar_consumo_vehiculo(self, identificador: str, kilometros: float) -> str:
        if not self.identificador_existe(identificador):
            return f"Error al consultar. Patente: {identificador} no está registrada en la flota"
        vehiculo = self.__dicc_vehiculos[identificador]
        consumo_vehiculo = round(vehiculo.calc_consumo(kilometros), 2)
        return f"| Consumo de {identificador} en {kilometros} km: {consumo_vehiculo} l|"
    
    def consumo_global(self, kilometros: float) -> float:
        total = 0
        for vehiculo in self.__dicc_vehiculos.values():
            total += vehiculo.calc_consumo(kilometros)
        return f"Consumo total de la flota: {round(total, 2)} l"
    
    def listado_consumos(self, kilometros: float) -> str:
        listado = "Lista de consumos individuales \n \n"
        for identificador in self.__dicc_vehiculos.keys():
            listado += self.consultar_consumo_vehiculo(identificador, kilometros) + "\n"
        return listado