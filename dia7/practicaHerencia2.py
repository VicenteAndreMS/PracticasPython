class Mascota:
    def __init__(self,edad,nombre,cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas

class Gato(Mascota):
    pass


morita = Gato(2,'Morita',4)
print((f"Nombre: {morita.nombre}"),(f"Edad: {morita.edad} años"),(f"Cantidad de patas: {morita.cantidad_patas}"))