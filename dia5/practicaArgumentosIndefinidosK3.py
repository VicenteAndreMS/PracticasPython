def describir_persona(nombre,**kwargs):
    print(f"Características de {nombre}:")
    for nombre_arg,valor_arg in kwargs.items():
        print(f"{nombre_arg}: {valor_arg}")



describir_persona('Vicente',y='uno',x='dos',a=0)
