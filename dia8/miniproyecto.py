def bienvenida():
    ("Bienvenido a la farmacia Pilar")


def decorador(rubro):
    print("\n" + "*" * 23)    
    print("Su número es: ")
    if rubro == 1:
        print(next(p))
    elif rubro == 2:
        print(next(f))
    else:
        print(next(c))
    print("Aguarde y será atendido")
    print("\n" + "*" * 23)    

def preguntar():
    bienvenida()
    seleccion_usuario_int = 0 
    while seleccion_usuario_int != 4:
        print("Escriba el número de opción a dónde quiere formarse")
        print("1. Perfumería")
        print("2. Farmacia")
        print("3. Cosméticos")
        print("4. Cerrar programa(SÓLO EMPLEADOS)")
        seleccion_usuario = input()
        seleccion_usuario_int = int(seleccion_usuario)
        if seleccion_usuario_int == 1:
            decorador(seleccion_usuario_int)
        elif seleccion_usuario_int == 2:
            decorador(seleccion_usuario_int)
        elif seleccion_usuario_int == 3:
            decorador(seleccion_usuario_int)            
        elif seleccion_usuario_int == 4:
            seleccion_usuario_int=4

            
def inicio():
    seleccion_usuario_int = 0 
    while seleccion_usuario_int != 4:
        preguntar()
        print("Escriba el número de opción a dónde quiere formarse")
        print("1. Perfumería")
        print("2. Farmacia")
        print("3. Cosméticos")
        print("4. Cerrar programa(SÓLO EMPLEADOS)")
        seleccion_usuario = input()
        seleccion_usuario_int = int(seleccion_usuario)
        if seleccion_usuario_int == 1:
            decorador(seleccion_usuario_int)
        elif seleccion_usuario_int == 2:
            decorador(seleccion_usuario_int)
        elif seleccion_usuario_int == 3:
            decorador(seleccion_usuario_int)            
        elif seleccion_usuario_int == 4:
            seleccion_usuario_int=4
    


def perfumeria():
    for x in range(1,10000):
        yield f"P - {x}"

def farmacia():
    for x in range(1,10000):
        yield f"F - {x}"

def cosmeticos():
    for x in range(1,10000):
        yield f"C - {x}"

p = perfumeria()
f = farmacia()
c = cosmeticos()

inicio()