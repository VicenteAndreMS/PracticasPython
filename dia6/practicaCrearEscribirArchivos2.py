file = open('mi_archivo.txt','a')

file.writelines('\nEsta es la segunda línea')

file.close()

file = open('mi_archivo.txt')

leer = file.read()
print(leer)

file.close()
