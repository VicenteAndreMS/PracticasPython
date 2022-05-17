lista_numeros = [1,3,-1,-5]
def todos_positivos(numeros):
    for numero in numeros:
        if numero < 0:
            return False
        else:
            pass

print(todos_positivos(lista_numeros))