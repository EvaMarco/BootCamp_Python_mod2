from FuncionesPrimerNivel001 import sumatodos

doble = lambda x: x*2

print(sumatodos(3, lambda x: x**3))

print(sumatodos(3, doble))
