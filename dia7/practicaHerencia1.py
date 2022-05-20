class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

vicente = Alumno('Vicente',24)
print(vicente.edad)