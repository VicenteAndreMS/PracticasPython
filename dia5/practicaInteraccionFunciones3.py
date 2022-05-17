import random

lista_numeros = ([1,2,3,4,5,6])
def lanzar_moneda():
    moneda = ['Sol','Águila']
    return random.choice(moneda)


def probar_suerte(cara,numeros):
    if cara == 'Sol':
        print("La lista se autodestruirá")
        numeros = []
    elif cara == 'Águila':
        print("La lista ha sido salvada")
    return numeros


print(probar_suerte((lanzar_moneda()),lista_numeros))