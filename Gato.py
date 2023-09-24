from Mamifero import Mamifero

class Gato(Mamifero):
    def __init__(self, nombre: str, tipo_animnal: str, edad: int, gestion: int,pedigri:str):
        super().__init__(nombre, tipo_animnal, edad, gestion)
        self.__pedigri = pedigri

    def set_pedigri(self,pedigri:str):
        self.__pedigri = pedigri

    def get_pedigri(self):
        return self.__pedigri
    
    def __str__(self):
        txt = super().__str__()
        txt += f"\nPedigri: {self.__pedigri}"
        return txt 