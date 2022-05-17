lista_numeros = [1,2,9,3,4,6,12,23,24]
def cantidad_pares(numeros):
    contador = 0
    resultado = 0
    for numero in numeros:
        if numero%2 == 0:
            contador += 1
            resultado += numero
        else:
            pass
    return contador,resultado



print("Números pares en total: ", (cantidad_pares(lista_numeros)[0]),"Suma total de pares: ", (cantidad_pares(lista_numeros)[1]))
