class Libro():
    def __init__(self,titulo,autor,cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas

    
mi_libro = Libro('Harry Potter','Pilar',650)
print(len(mi_libro))