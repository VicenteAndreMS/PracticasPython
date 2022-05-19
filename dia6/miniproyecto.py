from pathlib import Path
import os
import ntpath

def bienvenido():
    print("Bienvenido a recetas Pily")

def receta_home():
    receta_home_direccion = ntpath.basename("C:/Users/asrae/OneDrive/Escritorio/Vicente/SmartyDreams/Python/python-course/segundoCurso/dia6/Recetas")
    print("Las recetas están en: ",receta_home_direccion)

def menu():
    
    usuario_eleccion_int = 0
    while (usuario_eleccion_int < 6 and usuario_eleccion_int >= 0) or usuario_eleccion_int > 6:
        print("[1] Leer Receta")
        print("[2] Crear Receta")
        print("[3] Crear Categoría")
        print("[4] Eliminar receta")
        print("[5] Eliminar categoría")
        print("[6] Finalizar programa")
        usuario_eleccion = input("Ingrese la acción que desea realizar: ")
        usuario_eleccion_int = int(usuario_eleccion)
        if usuario_eleccion_int == 1:
            accion_uno(usuario_eleccion)
        elif usuario_eleccion_int == 2:
            accion_dos(usuario_eleccion)
        elif usuario_eleccion_int == 3:
            accion_tres(usuario_eleccion)
        elif usuario_eleccion_int == 4:
            accion_cuatro(usuario_eleccion)
        elif usuario_eleccion_int == 5:
            accion_cinco(usuario_eleccion)
        elif usuario_eleccion_int < 1 or usuario_eleccion_int > 6:
            print("Ingrese nuevamente otro número")
        elif usuario_eleccion_int == 6:
            print("FINALIZANDO PROGRAMA......")
            break

def accion_uno(usuario_eleccion_int):
    numero_categoria = 0
    lista = os.listdir("C:/Users/asrae/OneDrive/Escritorio/Vicente/SmartyDreams/Python/python-course/segundoCurso/dia6/Recetas")
    for categoria in lista:
        numero_categoria += 1
        print(f"{numero_categoria}. {categoria}")
    usuario_categoria = input("Ingresa la categoría deseada: ")
    if usuario_categoria in lista:
        if usuario_categoria == usuario_categoria:
            ruta_interna = Path("C:/Users/asrae/OneDrive/Escritorio/Vicente/SmartyDreams/Python/python-course/segundoCurso/dia6/Recetas")
            ruta_especifica = Path(ruta_interna/usuario_categoria)
            archivos_ruta = os.listdir(ruta_especifica)
            numero_receta = 0
            for receta in archivos_ruta:
                numero_receta += 1
                print(f"{numero_receta}. {receta}")
            usuario_receta = input("Elige la receta que deseas leer: \n")

            if usuario_receta in archivos_ruta:
                ruta_archivo = Path(usuario_receta)
                ruta_total = (ruta_especifica/ruta_archivo)
                abrir_archivo = open(ruta_total,'r')
                print("*************RECETA****************")
                print(f"La receta es:\n{abrir_archivo.read()}")
                abrir_archivo.close()
                print("***********TERMINADA**************")
            else:
                print("No se ingresó bien la el nombre de la receta, comience de nuevo")
                #print(archivo_receta.read_text())
                #archivo_receta.close()
            
            
        else:
            print("No se encuentra en la lista, repita de nuevo")

def accion_dos(usuario_eleccion_int):
    numero_categoria = 0
    lista = os.listdir("C:/Users/asrae/OneDrive/Escritorio/Vicente/SmartyDreams/Python/python-course/segundoCurso/dia6/Recetas")
    for categoria in lista:
        numero_categoria += 1
        print(f"{numero_categoria}. {categoria}")
    usuario_categoria = input("Ingresa la categoría en la que desea escribir la receta: ")
    if usuario_categoria in lista:
        nombre_receta = input("Escriba el nombre de la receta:\n")
        nombre_receta += ".txt"
        receta_nueva = input(f"Escriba la Receta: ")
        ruta_interna = Path("C:/Users/asrae/OneDrive/Escritorio/Vicente/SmartyDreams/Python/python-course/segundoCurso/dia6/Recetas")
        ruta_especifica = Path(ruta_interna/usuario_categoria)
        print(ruta_especifica)
        escribirNombreContenidoAccion2(nombre_receta,receta_nueva,ruta_especifica)
    else:
        print("Debía ingresar una categoría correcta, intente de nuevo")

def accion_tres(usuario_eleccion_int):
    lista = os.listdir("C:/Users/asrae/OneDrive/Escritorio/Vicente/SmartyDreams/Python/python-course/segundoCurso/dia6/Recetas")
    ruta_interna = Path("C:/Users/asrae/OneDrive/Escritorio/Vicente/SmartyDreams/Python/python-course/segundoCurso/dia6/Recetas")
    usuario_categoria = input("Escriba el nombre de la Categoría que desea crear: \n")
    if not usuario_categoria in lista:
        os.mkdir(f"{ruta_interna}/{usuario_categoria}")
        print("***************************************************")
        print("¡¡¡Se ha creado satisfactoriamente la Categoría!!!")
        print("***************************************************")
    else:
        print("Esa Categoría ya existe, inicie nuevamente")

def accion_cuatro(usuario_eleccion_int):
    numero_categoria = 0
    lista = os.listdir("C:/Users/asrae/OneDrive/Escritorio/Vicente/SmartyDreams/Python/python-course/segundoCurso/dia6/Recetas")
    for categoria in lista:
        numero_categoria += 1
        print(f"{numero_categoria}. {categoria}")
    usuario_categoria = input("Ingresa la categoría deseada: ")
    if usuario_categoria in lista:
        if usuario_categoria == usuario_categoria:
            ruta_interna = Path("C:/Users/asrae/OneDrive/Escritorio/Vicente/SmartyDreams/Python/python-course/segundoCurso/dia6/Recetas")
            ruta_especifica = Path(ruta_interna/usuario_categoria)
            archivos_ruta = os.listdir(ruta_especifica)
            numero_receta = 0
            for receta in archivos_ruta:
                numero_receta += 1
                print(f"{numero_receta}. {receta}")
            usuario_receta = input("Elige la receta que deseas eliminar: \n")

            if usuario_receta in archivos_ruta:
                ruta_archivo = Path(usuario_receta)
                ruta_total = (ruta_especifica/ruta_archivo)
                os.remove(f'{ruta_total}')
                print("*****************************************************")
                print("¡¡¡Se ha eliminado satisfactoriamente la Receta!!!")
                print("*****************************************************")
            else:
                print("No se ingresó bien el nombre de la receta, comience de nuevo")
            
            
        else:
            print("No se encuentra en la lista, repita de nuevo")

def accion_cinco(usuario_eleccion_int):
    numero_categoria = 0
    lista = os.listdir("C:/Users/asrae/OneDrive/Escritorio/Vicente/SmartyDreams/Python/python-course/segundoCurso/dia6/Recetas")
    ruta_interna = Path("C:/Users/asrae/OneDrive/Escritorio/Vicente/SmartyDreams/Python/python-course/segundoCurso/dia6/Recetas")
    for categoria in lista:
        numero_categoria +=1
        print(f"{numero_categoria}. {categoria}")
    usuario_categoria = input("Escriba el nombre de la Categoría que desea eliminar: \n")
    if usuario_categoria in lista:
        os.rmdir(f"{ruta_interna}/{usuario_categoria}")
        print("*****************************************************")
        print("¡¡¡Se ha eliminado satisfactoriamente la Categoría!!!")
        print("*****************************************************")
    else:
        print("Esa Categoría no existe, inicie nuevamente")

def escribirNombreContenidoAccion2(nombre_receta,receta_nueva,ruta_especifica):
    archivo = open(ruta_especifica/nombre_receta,'w')
    archivo.write(f"{receta_nueva}")
    archivo.close()
    print("************************************************")
    print("¡¡¡Se ha creado satisfactoriamente la receta!!!")
    print("************************************************")



bienvenido()
receta_home()
menu()