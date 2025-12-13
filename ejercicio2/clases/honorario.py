from clases.trabajador import Trabajador

valor_hora = 2000

class Honorario(Trabajador):
    def __init__(self, nombre_completo: str, rut: str, sueldo_base: float, estado: str, horas: float):
        super().__init__(nombre_completo, rut, sueldo_base, estado)
        self.__horas = horas
    
    def calcular_salario(self):
        return self.get_sueldo_base() + self.__horas * valor_hora