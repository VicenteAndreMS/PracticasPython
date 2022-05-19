from asyncore import read


archivo = "texto1.txt"
def abrir_leer(file):
    archivo_leido = open(file,'r')
    completo = archivo_leido.read()
    return completo


print(abrir_leer(archivo))