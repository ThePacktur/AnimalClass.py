from Animal import Animal

class Mamifero(Animal):
    def __init__(self, nombre: str, tipo_animnal: str, edad: int,gestion:int):
        super().__init__(nombre, tipo_animnal, edad)
        self.__gestion = gestion

    def set_gestion(self,gestion:int):
        self.__gestion = gestion

    def get_gestion(self):
        return self.__gestion
    
    def comer(self):
        print("Los mamiferos estan comiendo.")

    def __str__(self):
        txt = super().__str__()
        txt += f"\nGestion: {self.__gestion}"
        return  txt 

    