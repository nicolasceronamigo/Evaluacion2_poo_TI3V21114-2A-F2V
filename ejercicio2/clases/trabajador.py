class Trabajador:
    def __init__(self, nombre_completo: str, rut: str, sueldo_base: float, estado: str):
        self.__nombre_completo = nombre_completo
        self.__rut = rut
        self.__sueldo_base = sueldo_base
        self.__estado = estado
    
    def get_rut(self):
        return self.__rut
    
    def get_nombre_completo(self):
        return self.__nombre_completo
    
    def get_sueldo_base(self):
        return self.__sueldo_base
    
    def get_estado(self):
        return self.__estado

    def resumen(self):
        return f"| Nombre: {self.__nombre_completo} | RUT: {self.__rut} | Tipo: {type(self).__name__} | Sueldo Base: {self.__sueldo_base} | Salario Final: {self.calcular_salario()} |"