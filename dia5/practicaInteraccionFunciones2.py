lista_numeros = [1,5,3,5,2,1,3,3,3]

def reducir_lista(numeros):
    numeros.sort()
    comparador = 0
    for numero in numeros:
        if comparador < numero:
            comparador = numero
        elif comparador <= numero:
            comparador = numeros.index(numero)
            print(comparador)
            numeros.remove(numeros[numero])
    return numeros


print(reducir_lista(lista_numeros))        
