
class Banco():
    def __init__(self):
        self.__dicc_cuentas = {}
    
    def get_dicc_cuentas(self):
        return self.__dicc_cuentas
    
    def cuenta_existe(self, num_cuenta):
        if str(num_cuenta) in self.__dicc_cuentas.keys():
            return True
        return False
    
    def agregar_cuenta(self, cuenta):
        num_cuenta = cuenta.get_num_cuenta()
        if self.cuenta_existe(num_cuenta):
            return f"Error al agregar. Cuenta número: {num_cuenta} ya existe"
        self.__dicc_cuentas[str(num_cuenta)] = cuenta
        return f"Cuenta número: {num_cuenta} agregada"
    
    def consultar_cuenta_existe(self, num_cuenta):
        if self.cuenta_existe(num_cuenta):
            return f"Resultado consulta: n° cuenta {num_cuenta} existe"
        return f"Resultado consulta: n° cuenta {num_cuenta} no existe"
    
    def mostrar_historial_cuenta(self, num_cuenta):
        if self.cuenta_existe(num_cuenta):
            return self.__dicc_cuentas[str(num_cuenta)].mostrar_historial()
        return None
    
    def mostrar_saldo_tipo_cuentas(self):
        resultado = "Saldo y Tipo de las cuentas \n \n"
        for cuenta in self.__dicc_cuentas.values():
            resultado += cuenta.mostrar_saldo_tipo() + "\n"
        return resultado
    
    def mostrar_saldo_total(self):
        saldo_total = 0
        for cuenta in self.__dicc_cuentas.values():
            saldo_total += cuenta.get_saldo()
        return f"Saldo total: {saldo_total}"