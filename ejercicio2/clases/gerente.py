from clases.trabajador import Trabajador

class Gerente(Trabajador):
    def __init__(self, nombre_completo: str, rut: str, sueldo_base: float, estado: str, bono: float):
        super().__init__(nombre_completo, rut, sueldo_base, estado)
        self.__bono = bono
    
    def calcular_salario(self):
        return self.get_sueldo_base() + self.__bono