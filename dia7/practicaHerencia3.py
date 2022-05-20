class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass

class Automovil(Vehiculo):
    pass


print(Automovil.__base__)
print(Vehiculo.__subclasses__)