lista_numeros=[101,32,-300,9111,439,135,-20]
def suma_menores(numeros):
    resultado = 0
    for numero in numeros:
        if numero > 0 and numero < 1000:
            resultado += numero
        else:
            pass
    return resultado




print(suma_menores(lista_numeros))