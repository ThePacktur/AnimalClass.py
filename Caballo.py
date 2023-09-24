from Mamifero import Mamifero

class Caballo(Mamifero):
    def __init__(self, nombre: str, tipo_animnal: str, edad: int, gestion: int,comida:str,ejercicio:int):
        super().__init__(nombre, tipo_animnal, edad, gestion)
        self.__comida = comida
        self.__ejercicio = ejercicio

    def set_comida(self,comida:str):
        self.__comida = comida

    def get_comida(self):
        return self.__comida
    
    def set_ejercicio(self,ejercicio:int):
        self.__ejercicio = ejercicio

    def get_ejercicio(self):
        return self.__ejercicio
    
    def __str__(self):
        txt = super().__str__()
        txt += f"\nComida: {self.__comida}"
        txt += f"\nEjercicio: {self.__ejercicio}"
        return txt