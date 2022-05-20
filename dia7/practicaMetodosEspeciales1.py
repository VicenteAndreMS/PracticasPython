class Libro():
    def __init__(self,titulo,autor,cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_pagina = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

    
mi_libro = Libro('Harry Potter','Pilar',650)
print(mi_libro)