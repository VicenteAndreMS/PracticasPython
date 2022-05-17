from random import randint
import math
base = randint(1,10)
potencia_numero = randint(1,5)

def potencia(baseNum,potenciaNum):
    resultado = math.pow(baseNum,potenciaNum)
    return resultado
    




print(f"Base: {base} Potencia: {potencia_numero} Resultado: ",potencia(base,potencia_numero))