from asyncio.windows_events import INFINITE

def ciclo():
    for x in range(1,INFINITE):
        if (x%7) == 0:
            yield x
        else:
            continue

generador = ciclo()
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

