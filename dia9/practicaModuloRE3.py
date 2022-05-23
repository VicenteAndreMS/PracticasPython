import re
def verificar_cp(cp):
    patron = r'\^w{2}'
    resultado = re.search(patron,cp)
    if resultado == None:
        return "El código postal ingresado no es correcto"
    else:
        return "ok"

print(verificar_cp('AB'))