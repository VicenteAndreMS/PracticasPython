from random import randint

def lanzar_dados():
    dado1 = randint(1,6)
    dado2 = randint(1,6)
    return dado1,dado2


def evaluar_jugada(numero1,numero2):
        suma = numero1 + numero2
        print(numero1,numero2)
        if (suma) <= 6:
            print(f"La suma de tus dados es: {suma}. Lamentable")
        elif (suma) > 6 and (suma) <10:
            print(f"La suma de tus dados es {suma}. Tienes buenas chances")
        elif (suma) >= 10:
            print(f"La suma de tus dados es {suma}. Parece una jugada ganadora")
        
    






evaluar_jugada((lanzar_dados()[0]),(lanzar_dados()[1]))