from Mamifero import Mamifero

class Perro(Mamifero):
    def __init__(self, nombre: str, tipo_animnal: str, edad: int, gestion: int,raza:str):
        super().__init__(nombre, tipo_animnal, edad, gestion)
        self.__raza = raza

    def set_raza(self,raza:int):
        self.__raza = raza

    def get_raza(self):
        return self.__raza
    
    def __str__(self):
        txt = super().__str__()
        txt += f"\nRaza: {self.__raza}"
        return txt  
    
