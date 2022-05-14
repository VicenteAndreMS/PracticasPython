esp = ['uno','dos','tres','cuatro','cinco']
port = ['um','dois','trës','quatro','cinco']
engl = ['one','two','three','four','five']

numeros = list(zip(esp,port,engl))
for indice, numero in enumerate(numeros):
    print(f"{indice}. {numero}\n")