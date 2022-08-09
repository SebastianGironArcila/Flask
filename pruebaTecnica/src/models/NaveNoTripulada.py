
from src.models.Nave import Nave


class NaveNoTripulada(Nave):
    def __init__(self, idNave: int, tipoDeNave: str, nombre: str, peso: float, combustible: str, velocidad: float, activo: bool) -> None:
        super().__init__(idNave, tipoDeNave, nombre, peso, combustible)
        self.velocidad = velocidad
        self.activo = activo

    def abastecer(self):
        pass

    def limpiar(self):
        pass

    def regular(self):
        pass

    def despegar(self):
        pass
    
    def aterrizar(self):
        pass

