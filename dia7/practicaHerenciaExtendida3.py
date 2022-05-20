class Padre:
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
    
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"

gael = Hijo()
print(gael.hobby())
print(gael.reir())
