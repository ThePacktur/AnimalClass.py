from Reptil import Reptil

class Serpiente(Reptil):
    def __init__(self, nombre: str, tipo_animnal: str, edad: int, ubicacion: str):
        super().__init__(nombre, tipo_animnal, edad, ubicacion)
        
    def __str__(self):
        txt = super().__str__()
        return txt