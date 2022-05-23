contenido = []
numeros = [3,2,1,0]
def vidas():
    for x in range(3,-1,-1):
        if x > 0:
            contenido = (f"Te quedan {x} vidas")
            yield contenido
        elif x == 0:
            contenido = ("Game Over")
            yield contenido

perder_vida = vidas()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))