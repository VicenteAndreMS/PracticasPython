class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amantar(self):
        print("Amamantando crías")
    
class Ornitorrinco(Ave,Pez,Mamifero):
    venenoso = True

orni1 = Ornitorrinco()
orni1.poner_huevos()
print(orni1.tiene_pico)
print(orni1.vertebrado)
print(orni1.venenoso)
orni1.nadar()
orni1.caminar()
orni1.amantar()

