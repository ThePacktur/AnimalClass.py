from Animal import Animal

class Reptil(Animal):
    def __init__(self, nombre: str, tipo_animnal: str, edad: int,ubicacion:str):
        super().__init__(nombre, tipo_animnal, edad)
        self.__ubicacion = ubicacion

    def set_ubicacion(self,ubicacion):
        self.__ubicacion = ubicacion

    def get_ubicacion(self):
        return self.__ubicacion
    
    def comer(self):
        print("Reptieles Comiendo no molestar")

    def caminar(self):
        print("Se acercan los reptiles corre!!!")

    def __str__(self):
        txt = super().__str__()
        txt += f"\nUbicacion: {self.__ubicacion}"
        return txt