import requests
import bs4

#Crear URL sin número de página
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

#Lista de títulos con 4 o 5 estrellas
titulos_rating_alto = []

#Iterar páginas
for pagina in range(1,51):
    
    #Crear sopa en cada página
    url_pagina = (url_base.format(pagina))
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text,'lxml')

    #Seleccionar datos de libros
    libros = sopa.select('.product_pod')

    #Iterar en los libros
    for libro in libros:
        
        #Chequear que tengan 4 o 5 estrellas
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:

            #Guardar título en variable
            titulo_libro = libro.select('a')[1]['title']

            #Agregar libro a la lista
            titulos_rating_alto.append(titulo_libro)

#Ver los libros de 4 y 5 estrellas
for t in titulos_rating_alto:
    print(t)