from collections import deque
lista = ['Londres','Berlín','París','Madrid','Roma','Moscú']
lista_ciudades = deque(lista)
ancho = len(lista_ciudades)-1
for numero in range(ancho,2,-1):
    lista_ciudades.remove(lista_ciudades[numero])



print(lista_ciudades)
