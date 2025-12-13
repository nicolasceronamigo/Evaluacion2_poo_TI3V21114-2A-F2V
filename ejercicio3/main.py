from clases.cuenta_ahorro import CuentaAhorro
from clases.cuenta_corriente import CuentaCorriente
from clases.banco import Banco

c_corriente1 = CuentaCorriente(1, "nom_c_corriente1", 10000)
c_corriente2 = CuentaCorriente(2, "nom_c_corriente2", 20000)

c_ahorro1 = CuentaAhorro(5, "nom_c_ahorro5", 50000)
c_ahorro2 = CuentaAhorro(6, "nom_c_ahorro6", 60000)

lista_cuentas = [c_ahorro1, c_ahorro2, c_corriente1, c_corriente2]

banco1 = Banco()

for cuenta in lista_cuentas:
    banco1.agregar_cuenta(cuenta)

print("------------------------------------------------------------------------------\n")

print(c_corriente1.retirar(10000))
print(c_corriente1.depositar(50000))

print("------------------------------------------------------------------------------\n")

print(c_corriente2.retirar(20000))
print(c_corriente2.depositar(25000))

print("------------------------------------------------------------------------------\n")

print(c_ahorro1.retirar(10000))
print(c_ahorro1.depositar(50000))
print(c_ahorro1.saldo_interes())

print("------------------------------------------------------------------------------\n")

print(c_ahorro2.retirar(10000))
print(c_ahorro2.depositar(50000))
print(c_ahorro2.saldo_interes())

print("------------------------------------------------------------------------------\n")

print(banco1.mostrar_saldo_tipo_cuentas())

print("------------------------------------------------------------------------------\n")

print(banco1.mostrar_historial_cuenta(1))

print("------------------------------------------------------------------------------\n")
print(banco1.mostrar_historial_cuenta(2))

print("------------------------------------------------------------------------------\n")
print(banco1.mostrar_historial_cuenta(5))

print("------------------------------------------------------------------------------\n")

print(banco1.mostrar_historial_cuenta(6))

print("------------------------------------------------------------------------------\n")

print(banco1.mostrar_saldo_total())

print("------------------------------------------------------------------------------\n")