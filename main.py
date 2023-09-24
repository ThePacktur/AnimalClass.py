from Animal import Animal
from Mamifero import Mamifero
from Perro import Perro
from Gato import Gato
from Caballo import Caballo
from Reptil import Reptil
from Serpiente import Serpiente

animal1 = Animal("Ornitorinco","Mamifero-acuatico",5)
mamifero1 = Mamifero("Vaca","Obino",7,20)
perro1 = Perro("Washinton","Canino",12,15,"BullTerryer-Chile")
gato1 = Gato("Leela","Felinio",15,34,"beto")
caballo1 = Caballo("Padrino","Equino",5,23,"Heno",24)
reptil1 = Reptil("Turtle", "Tortuga-leon",120,"africa")
serpiente1 = Serpiente("Stangula","serpiente",17,"africa")

print(animal1)
print("-------------")
print(mamifero1)
print("-------------")
print(perro1)
print("-------------")
print(gato1)
print("-------------")
print(caballo1)
print("-------------")
print(reptil1)
print("-------------")
print(serpiente1)