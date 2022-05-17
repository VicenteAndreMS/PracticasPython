import random
import string
#Establecemos las palabras aleatorias
palabras = ["Vicente","Andre","Minero","Salazar"]
#Bienvenida
def bienvenida():
    print("Bienvenido al AHORCADO")
#Aquí se hace la elección de la palabra aleatoria
def elegir_palabra(palabras):
    palabra = random.choice(palabras)
    print(palabra)
    return palabra
#Mostramos los primeros guiones
def mostrar_guiones(palabra_aleatoria):
    guiones = []
    for letras in palabra_aleatoria:
        guiones += '_'
    print(guiones)
    #Llamamos a la función pedir_letra
    pedir_letra(palabra_aleatoria)
#En esta función le pedimos al usuario que ingrese una letra,
#después de eso intentamos buscar la letra del usuario en la palabra aleatoria
def pedir_letra(palabra_aleatoria):
    #6 intentos
    intentos = 6
    #Pasamos a minúscula a la palabra aleatoria
    palabra_minus = palabra_aleatoria.lower()
    palabra_resultado = []
    palabra_unida = []
    print(palabra_minus)
    #Ciclo que se hará mientras los intentos sean mayor a 0
    while intentos > 0:
        #Pedimos el ingreso de la letra
        letra_usuario = input("Ingrese una letra: ")
        #Si la letra está dentro de la palabra en minúsculas valoramos que no se haya 
        #ingresado antes y también vamos concatenando los valores ingresados con el
        #usuario que coincidan con la palabra
        if letra_usuario in palabra_minus:
            #Se imprime las vidas que tiene,
            #Se concatena las letras ingresadas por el usuario a palabra_resultado
            #Se hace un join de la palabra resultado y se compara con la palabra_minus
            print(f"Bien hecho, tienes {intentos} vidas")
            palabra_resultado += letra_usuario
            palabra_unida = ''.join(palabra_resultado)
            print(palabra_unida)
            print(palabra_minus)
            if palabra_unida == palabra_minus:
                print("¡FELICIDADES, GANASTE!")            
                break
            else:
                continue
        #Si la letra no se encuentra entonces descontamos una vida y mandamos mensaje de error
        elif not letra_usuario in palabra_minus:
            intentos -=1
            print(f"Esta letra NO se encuentra dentro, te quedan {intentos} vidas")
        #Si la longitud de la letra es diferente de 1 o no es una letra entonces se descuenta 1 vida y se imprime un mensaje
        elif len(letra_usuario) != 1 or not string(letra_usuario):
            intentos -=1
            print(f"Ingresa SOLO 1 letra, te quedan {intentos} vidas")    
    else:
        print("LÁSTIMA :(")
        

bienvenida()
mostrar_guiones(elegir_palabra(palabras))

