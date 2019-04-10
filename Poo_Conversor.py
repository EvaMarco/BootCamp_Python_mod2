class Termometro:
    def __init__(self):
        self.__unidad = 'C'
        self.__temperatura = 0

    def __conversor(self, temperatura, unidad):
        if unidad == 'C':
            return '{}ºF'.format(int(temperatura) * 9/5 + 32)
        elif unidad == 'F':
            return '{}º C.'.format(int(temperatura - 32) * (5/9))
        else:
            return 'Unidad incorrecta'

    def __str__(self):
        return '{}º{}.'.format(self.__temperatura, self.__unidad)


# Vamos a hacer un metodo setter y getter para las unidades y otro para las temperatuas.
    def unidadmedida(self, uni = None):

        if uni == None:

            return 'Las unidades son {}.'.format(self.__unidad)
        else:
            if uni == 'F' or uni == 'C':
                self.__unidad = uni
                
    def temp(self, temperatura=None):

        if temperatura == None:
            return '{}º.'.format(self.__temperatura)
        else:
            self.__temperatura = temperatura
   
    def mide(self, unim=None):

        if unim == None or unim == self.__unidad:
            return self.__str__()
        else:
            return self.__conversor(self.__temperatura, self.__unidad)
