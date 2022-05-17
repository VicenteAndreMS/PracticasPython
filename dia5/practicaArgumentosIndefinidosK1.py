from unittest import result


def cantidad_atributos(**kwargs):
    resultado = 0
    for clave,valor in kwargs.items():
        resultado+=1
    
    return resultado

print(cantidad_atributos(x=2,y=3,z=1,a=1))
