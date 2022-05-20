class Libro():
    def __init__(self,titulo,autor,cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print( "Se ha eliminado el LIBRO")


    
mi_libro = Libro('Harry Potter','Pilar',650)

del mi_libro
print(len(mi_libro))