class Personaje:
    real = False

    def __init__(self,especie,magico,edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad

harry_potter = Personaje('Humano',True,17)

print(harry_potter.especie,harry_potter.magico,harry_potter.edad)