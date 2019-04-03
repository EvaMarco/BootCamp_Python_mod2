def normal(x):
    return x


def cuadrado(x):
    return x*x


def sumatodos(limite, f):
    resultado = 0
    for i in range(limite + 1):
        resultado += f(i)
    return resultado


if __name__ == '__main__':
    print(sumatodos(100, normal))
    print(sumatodos(3, cuadrado))
