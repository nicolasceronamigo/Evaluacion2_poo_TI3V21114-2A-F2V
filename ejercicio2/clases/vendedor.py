from clases.trabajador import Trabajador

comision = 5 #porcentual 5%

class Vendedor(Trabajador):
    def __init__(self, nombre_completo: str, rut: str, sueldo_base: float, estado: str, ventas_mes: float):
        super().__init__(nombre_completo, rut, sueldo_base, estado)
        self.__ventas_mes = ventas_mes
    
    def calcular_salario(self):
        return self.get_sueldo_base() + self.__ventas_mes * comision / 100
    
    