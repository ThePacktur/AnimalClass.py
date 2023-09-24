class Animal:
    def __init__(self,nombre:str,tipo_animnal:str,edad:int):
        self.__nombre = nombre
        self.__tipo_animal = tipo_animnal
        self.__edad = edad
       

    def set_nombre(self,nombre:str):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_tipo_animal(self,tipo_animal:str):
        self.__tipo_animal = tipo_animal

    def get_tipo_animal(self):
        return self.__tipo_animal

    def set_edad(self,edad:str):
        self.__edad = edad
    
    def get_edad(self,):
        return self.__edad

    def comer(self):
        print("Animales comiendo")

    def caminar(self):
        print("El animal se desplaza")
    
    def __str__(self):
        txt = f"Nombre: {self.__nombre}"
        txt += f"\nTipo_animal: {self.__tipo_animal}"
        txt += f"\nEdad: {self.__edad}"
        return txt