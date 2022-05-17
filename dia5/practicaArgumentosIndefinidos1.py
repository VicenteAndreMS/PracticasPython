def suma_cuadrados(*args):
    total = 0
    for arg in args:
        total += arg*arg
    return total

print(suma_cuadrados(2,1,3))