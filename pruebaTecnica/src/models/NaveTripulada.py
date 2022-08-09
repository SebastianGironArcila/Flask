from src.models.Nave import Nave


class NaveTripulada(Nave):
    def __init__(self, idNave: int, tipoDeNave: str, nombre: str, peso: float, combustible: str, tarea :str, capacidad: str) -> None:
        super().__init__(idNave, tipoDeNave, nombre, peso, combustible)
        self.tarea = tarea
        self.capacidad = capacidad

    def raparacion(self):
        pass

    def matenimiento(self):
        pass

    def investigacion(self):
        pass

    def despegar(self):
        pass
    
    def aterrizar(self):
        pass