class Perro():
    
    # Función constructor. El primer parámetro será self.
    def __init__(self, n, e, p):
        # Esto son los atributos.
        self.nombre = n
        self.edad = e
        self.peso = p
    # Estos son los métodos de la clase.

    def ladrar(self):
        if self.peso >= 8:
            print('GUAU GUAU')
        else:
            print('guau guau')

    def __str__(self):
        return 'Soy el perro {}, con e = {} y p = {}'.format(self.nombre, self.edad, self.peso)


class Perroasistencia(Perro):
    # Aquí hacemos una llamada a los métodos de su clase. 
    def __init__(self, nombre, edad, peso, amo):
        Perro.__init__(self, nombre, edad, peso)
        self.amo = amo
        # Al ponerle dos guiones por delante, simulamos los atributos privados.
        self.__trabajando = False

    # Esto es sobreescribir un método.

    def __str__(self):
        return 'Soy el perro {} de asistencia de {}, con e = {} y p = {}'.format(self.nombre, self.amo,  self.edad, self.peso)
    # Vamos a crear métodos nuevos que lo diferencien de la clase principal.
    
    def pasear(self):
        print('{} ayuda a su dueño {} a pasear.'.format(self.nombre, self.amo))
              
    def ladrar(self):
        if self.__trabajando:
              print('Shhh, no puedo ladrar estoy trabajando')
        else:
            # Si se cambia la clase al llamar a self, no hará falta buscarlo en todos los sitios y aquí estará cambiado.
            Perro.ladrar(self)
            
    def trabajando(self, valor=None):
        # Si no informas el valor te devuelve en que estado esta.
        if valor == None:
            return self.__trabajando
        # Si lo informas le cambia el valor. 
        else:
            self.__trabajando = valor
