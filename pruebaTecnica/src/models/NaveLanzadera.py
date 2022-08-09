from src.models.Nave import Nave


class NaveLazadera(Nave):
    def __init__(self, idNave: int, tipoDeNave: str, nombre: str, peso: float, combustible: str, empuje: float, altura:float , potencia: float, carga: str) -> None:
        super().__init__(idNave, tipoDeNave, nombre, peso, combustible)
        self.empuje = empuje
        self.altura = altura
        self.potencia = potencia
        self.carga = carga

    def cargar(self):
        pass

    def descargar(self):
        pass

    def despegar(self):
        pass
    
    def aterrizar(self):
        pass

    