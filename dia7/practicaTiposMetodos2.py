class Jugador:

    vivo = False

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(f"Jugador vivo: {cls.vivo}")

Jugador.revivir()