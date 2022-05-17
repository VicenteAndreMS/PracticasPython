def suma_absolutos(*args):
    total = 0
    for arg in args:
        if arg < 0:
            total += -(arg)
        elif arg >= 0:
            total += arg
    return total

print(suma_absolutos(1,2,-3,-12,-7,10))
