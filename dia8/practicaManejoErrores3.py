from pathlib import Path


def abrir_archivo(nombre_archivo):
    try:
        print("Abriendo exitosamente")
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("Archivo no encontrado")
    except: 
        print("Error desconocido")
    finally:
        print("Finalizando ejecución")


abrir_archivo(Path("C:/Users/asrae/OneDrive/Escritorio/Vicente/Infosys/Documentación3/INE - VICENTE MINERO.pdf"))
