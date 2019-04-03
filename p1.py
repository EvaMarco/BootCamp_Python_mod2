def sumatodo(limits):
    resultado = 0
    for i in range( 0, limits +1):
        resultado += i
    return resultado

def sumatodocuadrado(limite):
    resultado = 0
    for i in range(limite+1):
        resultado += i**2
    return resultado

print(sumatodocuadrado(3))
    

print(sumatodo(100))