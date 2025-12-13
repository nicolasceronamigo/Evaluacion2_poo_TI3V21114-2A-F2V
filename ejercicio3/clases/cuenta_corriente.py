from clases.cuenta import Cuenta

credito = -50000
class CuentaCorriente(Cuenta):
    def retirar(self, monto: float):
        if self.get_saldo() >= monto:
            return super().retirar(monto)
        elif self.get_saldo() - monto >= credito:
            self.set_saldo(self.get_saldo() - monto)
            self.get_hist_movimientos().append(f"Retiro {monto}")
            return f"Retiro de {monto} realizado"
        return f"El retiro de {monto} supera el crédito de la cuenta"