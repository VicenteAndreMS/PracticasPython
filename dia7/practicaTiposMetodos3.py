class Persona:

    def lanzar_flecha(self,cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas
        cantidad_flechas -= 1
        print(f"La cantidad de flechas restantes son: {cantidad_flechas}")

personaje = Persona()

personaje.lanzar_flecha(39)

        
