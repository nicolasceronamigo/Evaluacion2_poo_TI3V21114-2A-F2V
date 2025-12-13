
class Cuenta:
    def __init__(self, num_cuenta: int, nombre_titular: str, saldo: float):
        self.__num_cuenta = num_cuenta
        self.__nombre_titular = nombre_titular
        self.__saldo = saldo
        self.__tipo = type(self).__name__
        self.__historial_movimientos =[]
    
    def get_num_cuenta(self):
        return self.__num_cuenta
    
    def get_saldo(self):
        return self.__saldo
    
    def set_saldo(self, saldo):
        self.__saldo = saldo
    
    def get_hist_movimientos(self):
        return self.__historial_movimientos
    
    def depositar(self, monto):
        if monto <= 0:
            return f"No se pueden depositar montos negativos o nulos"
        self.__saldo += monto
        self.__historial_movimientos.append(f"Déposito {monto}")
        return f"Depósito de {monto} realizado"
        
    def retirar(self, monto):
        if monto <= 0:
            return f"Monto a retirar debe ser positivo"
        elif self.__saldo < monto:
            return f"Saldo insuficiente para retirar {monto}"
        self.__saldo -= monto
        self.__historial_movimientos.append(f"Retiro {monto}")
        return f"Retiro de {monto} realizado"
    
    def mostrar_saldo_tipo(self):
        return f"| Saldo: {self.__saldo} | Tipo: {self.__tipo} |"
    
    def mostrar_historial(self):
        resultado = f"Historial de cuenta: {self.__num_cuenta} \n \n"
        for movimiento in self.__historial_movimientos:
            resultado += movimiento + "\n"
        return resultado