
def maxi(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for x in range(1, len(l)):
        if l[x] > m:
            m = l[x]
    return m


def mini(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for j in range(1, len(l)):
        if l[j] < m:
            m = l[j]
    return m


def media(*l):
    if len(l) == 0:
        return object
    suma = 0
    for valor in l:
        suma += valor
    return suma / len(l)


funciones = {
    'max': maxi,
    'min': mini,
    'media': media}


def returnf(nombre):
    nombre = nombre.lower
    if nombre in funciones.keys():
        return funciones[nombre]
    return None

