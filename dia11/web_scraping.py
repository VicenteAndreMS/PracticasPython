from turtle import title
import bs4
import requests

#https://escueladirecta-blog.blogspot.com/
resultado = requests.get('https://escueladirecta-blog.blogspot.com/')

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
parrafo_especial = sopa.select('p')
print(parrafo_especial)