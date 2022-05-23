import re
def verificar_saludo(frase):
    patron = r'^Hola'
    resultado = re.search(patron,frase)
    if not resultado:
        return "No has saludado"
    else:
        return "Ok"


print(verificar_saludo("Hola, qué tal"))
