from abc import ABC, abstractmethod

class Nave(ABC):
    def __init__(self,idNave:int,tipoDeNave:str,nombre:str, peso:float, combustible:str) -> None:
        self.id = idNave
        self.tipoDeNave = tipoDeNave
        self.nombre = nombre
        self.peso = peso
        self.combustible = combustible

    @abstractmethod
    def despegar(self):
        pass
    
    @abstractmethod
    def aterrizar(self):
        pass