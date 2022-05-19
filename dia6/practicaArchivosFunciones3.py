file = "texto2.txt"
def error_register(file):
    file = open(file,'a')
    file.write("\nAn error execution has been registered")
    file.close()

error_register(file)