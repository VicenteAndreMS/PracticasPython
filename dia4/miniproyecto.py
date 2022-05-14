from random import randint

nombre = input("¿Cómo te llamas?")
print(f"Bienvenido {nombre}, tienes 8 intentos para adivinar el número que está en el rango 1 a 50")
intentos = 7
numero_intento = 0
aleatorio = randint(1,50)
while (intentos>=0):
    numero_adivinado = int(input("¿Cuál número crees que es?"))
    numero_intento += 1
    if(numero_adivinado == aleatorio):
        print(f"¡¡¡¡¡¡¡Felicidades, adivinaste el número en el intento {numero_intento}!!!!!")
        break
    elif(numero_adivinado > 50 or numero_adivinado < 0):
        print(f"Por favor, ingresa una número entre 1 y 50. INTENTOS RESTANTES: {intentos}")
        intentos-= 1
    elif(numero_adivinado > aleatorio):
        print(f"El número que tienes que adivinar es MENOR. INTENTOS RESTANTES: {intentos}")
        intentos-= 1
    elif(numero_adivinado < aleatorio):
        print(f"El número que tienes que adivinar es MAYOR. INTENTOS RESTANTES: {intentos}")
        intentos-= 1
else:
    print(f" :(   GAME OVER - El número era: {aleatorio}      ):")