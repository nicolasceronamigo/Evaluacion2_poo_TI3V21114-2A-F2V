from clases.cuenta import Cuenta

interes_mensual = 0.5 #porcentual 0.5%

class CuentaAhorro(Cuenta):
    def saldo_interes(self):
        monto_interes = self.get_saldo() * interes_mensual / 100
        nuevo_saldo = self.get_saldo() + monto_interes
        self.set_saldo(nuevo_saldo)
        movimiento = f"Interés {monto_interes}"
        self.get_hist_movimientos().append(movimiento)
        return f"Se suma al saldo como interes: {monto_interes}"