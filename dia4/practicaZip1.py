capitales = ['Berlín','Tokio','París','Helsinki','Ottawa','Canberra']
paises = ["Alemania",'Japón',"Francia",'Finlandia','Canadá','Australia']
combo = list(zip(capitales,paises))

for capital,pais in combo:
    print(f"La capital de {pais} es {capital}");