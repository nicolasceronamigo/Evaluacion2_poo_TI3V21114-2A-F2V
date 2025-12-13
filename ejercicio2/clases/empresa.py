from clases.trabajador import Trabajador
from clases.gerente import Gerente
from clases.honorario import Honorario
from clases.vendedor import Vendedor

class Empresa:
    def __init__(self):
        self.__lista_trabajadores = []
    
    def trabajador_existe(self, trabaja):
        for trabajador in self.__lista_trabajadores:
            if trabajador.get_rut() == trabaja.get_rut():
                return True
        return False
    
    #Agregar nuevos trabajadores indicando su tipo y la información asociada. 
    def agregar_trabajador(self, tipo: str, *args) -> str:
        match tipo:
            case "Gerente":
                gerente = Gerente(*args)
                if self.trabajador_existe(gerente):
                    return f"Error al agregar. Gerente {gerente.get_nombre_completo()} ya existe"
                self.__lista_trabajadores.append(gerente)
                return f"Gerente {gerente.get_nombre_completo()} agregado"
            case "Honorario":
                honorario = Honorario(*args)
                if self.trabajador_existe(honorario):
                    return f"Error al agregar.Honorario {honorario.get_nombre_completo()} ya existe"
                self.__lista_trabajadores.append(Honorario(*args))
                return f"Honorario {honorario.get_nombre_completo()} agregado"
            case "Vendedor":
                vendedor = Vendedor(*args)
                if self.trabajador_existe(vendedor):
                    return f"Error al agregar. Vendedor {vendedor.get_nombre_completo()} ya existe"
                self.__lista_trabajadores.append(Vendedor(*args))
                return f"Vendedor {vendedor.get_nombre_completo()} agregado"
            case _:
                return f"Tipo {tipo} no existe."
    
    def incorporar_trabajador(self, trabajador):
        if self.trabajador_existe(trabajador):
            return f"Error al incorporar. Trabajador {trabajador.get_nombre_completo()} ya existe"
        self.__lista_trabajadores.append(trabajador)
        return f"{type(trabajador).__name__} {trabajador.get_nombre_completo()} incorporado"
    
    def filtrar_activos(self) -> list:
        lista_activos = []
        for trabajador in self.__lista_trabajadores:
            if trabajador.get_estado() == "Activo":
                lista_activos.append(trabajador)
        return lista_activos
    
    def listar_activos(self) -> str:
        resultado = "Listado de trabajadores activos \n \n"
        for trabajador in self.filtrar_activos():
            resultado += trabajador.resumen() + "\n"
        return resultado
    
    def listar_todos(self) -> str:
        resultado = "Listado de trabajadores \n \n"
        for trabajador in self.__lista_trabajadores:
            resultado += trabajador.resumen() + "\n"
        return resultado
    
    def calc_gasto_total(self) -> float:
        gasto_total = 0
        for trabajador in self.filtrar_activos():
            gasto_total += trabajador.calcular_salario()
        return gasto_total
    
    def lista_mayor_salario(self):
        lista_activos = self.filtrar_activos()
        def get_salario(trabajador):
            return trabajador.calcular_salario()
        lista_activos.sort(key = get_salario, reverse = True)
        resultado = "Lista trabajadores con mayor salario \n \n"
        for trabajador in lista_activos:
            resultado += trabajador.resumen() + "\n"
        return resultado
    
    def reporte(self):
        resultado = "Reporte salarios: \n \n"
        lista_activos = self.filtrar_activos()
        for trabajador in lista_activos:
            resultado += f"| Nombre: {trabajador.get_nombre_completo()} | Tipo: {type(trabajador).__name__} | Salario final: {trabajador.calcular_salario()} |\n"
        resultado += f"Gasto total en salarios: {self.calc_gasto_total()}"
        return resultado