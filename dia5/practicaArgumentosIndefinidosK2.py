def lista_atributos(**kwargs):
    resultado = 0
    for clave,arg in kwargs.items():
        resultado += arg
    return resultado

print(lista_atributos(y=0,a=3,z=10))