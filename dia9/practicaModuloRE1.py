import re

def verificar_email(usuario):
    correo = r'^\w+@\w+\.com$'  
    resultado = re.search(correo,usuario)
    if resultado == None:
        return"La dirección de email es incorrecta"
    else:
        return "Ok"


print(verificar_email('aaa@aaa.com'))