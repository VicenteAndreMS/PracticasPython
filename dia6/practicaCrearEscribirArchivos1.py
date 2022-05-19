#Abrir archivo en modo escritura
file = open('mi_archivo.txt','w')
#Sobreescribir "Nuevo texto"
file.write("Nuevo texto")
#Cerrar archivo
file.close()
#Abrir archivo modo lectura
file = open('mi_archivo.txt','r')
#Leer archivo
leer = file.read()
#Imprimir lectura
print(leer)
#Cerrar archivo
file.close()