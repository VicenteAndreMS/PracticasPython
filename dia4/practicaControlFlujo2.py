edad = 16
tiene_licencia = False

if (edad > 18) and (tiene_licencia == True):
    print("Puedes conducir")
elif (edad < 18) and (tiene_licencia == False):
    print("No puedes conducir aún. Debes tener 18 años y contar con una licencia")
elif (edad > 18) and (tiene_licencia == False):
    print("No puedes conducir. Necesitas contar con una lciencia")