from functools import reduce
lista = [1, 3, -1, 15, 9]

listadobles = map(lambda x: x*2, lista)
listapares = filter(lambda x: x % 2 == 0, lista)

sumatodo = reduce(lambda x, y: x + y, lista)
suma100 = reduce(lambda x, y: x+y, range(101))

print(list(listapares))
print(list(listadobles))
print(sumatodo)
print(suma100)
