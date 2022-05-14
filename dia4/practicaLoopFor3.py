lista_numeros = [1,6,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0

for numero in lista_numeros:
    if (numero%2 == 0):
        suma_pares += numero
    elif (numero%2 != 0):
        suma_impares += numero   

print(f"Números pares total: {suma_pares}")
print(f"Números impares total: {suma_impares}")