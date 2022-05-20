class Alarma:
    def postergar(self,cantidad_minutos):
        self.cantidad_minutos = cantidad_minutos
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")



alarma_objeto = Alarma()
alarma_objeto.postergar(15)