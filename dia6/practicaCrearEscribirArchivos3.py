list_values = ["Federico","20/12/2021","08:17:32","Sin errores de carga"]
file = open('register.txt','a')
#Aquí iteramos cada uno de los valores de la lista, a su vez que lo escribimos
#dentro del archivo
for word in list_values:
    file.writelines(word + "\n")

file.close()

file = open('register.txt','r')

read = file.read()
print(read)

file.close()

