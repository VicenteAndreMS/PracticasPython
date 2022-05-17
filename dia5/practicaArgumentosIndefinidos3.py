def numeros_persona(nombre,*args):
    suma_numeros = 0
    for arg in args:
        suma_numeros += arg
    print(f"{nombre}, la suma de tus números es: {suma_numeros}")


numeros_persona('Vicente',10,5,2,3)
