class Termometro:
    # Función constructora.
    
    def __init__(self):
        # Atributos iniciales. Son privados, no se pueden consultar.
        self.__unidad = 'C'
        self.__temperatura = 0

    # La función que informa del estado, la podemos usar en el print.
    def __str__(self):
        return '{}º{}.'.format(self.__temperatura, self.__unidad)


    # Vamos a hacer un metodo setter y getter para las unidades y otro para las temperatuas.

    def unidadmedida(self, uni = None):
    # Como los atributos son privados con esta función podemos consultarlos.
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

    # La función que nos cambia de unidades. Es privada porque no nos interesa que pueda ser llamada desde fuera.
    def __conversor(self, temperatura, unidad):
        if unidad == 'C':
            return '{}ºF'.format(int(temperatura) * 9/5 + 32)
        elif unidad == 'F':
            return '{}º C.'.format(int(temperatura - 32) * (5/9))
        else:
            return 'Unidad incorrecta'
        
    # Esta es la funcionalidad del termometro.
    
    def mide(self, unim=None):
    
        if unim == None or unim == self.__unidad:
            return self.__str__()
        else:
            if unim == 'F' or unim == 'C'
                return self.__conversor(self.__temperatura, self.__unidad)
            else:
                return self.__str__()
