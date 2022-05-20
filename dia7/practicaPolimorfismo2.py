class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con Katana")

erick = Mago()
choro = Arquero()
vicente = Samurai()

lista = [erick,choro,vicente]


for elemento in lista:
    elemento.atacar()

#def ataques(lista):
#    for persona in lista:
#        print(f"{persona} ha hecho un {persona.atacar()}")

#ataques(lista)