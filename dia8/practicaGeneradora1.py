from asyncio.windows_events import INFINITE


x = 1
def ciclo():
    for x in range(1,INFINITE):
        yield x


generador = ciclo()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))