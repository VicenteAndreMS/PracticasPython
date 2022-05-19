from pathlib import Path

ruta = Path("C:/Users/asrae/OneDrive/Escritorio/Vicente/SmartyDreams/Python/python-course/alternative")
alternativeRute = ruta / "prueba_python.txt"

file = open(alternativeRute)

print(file.read())

file.close()