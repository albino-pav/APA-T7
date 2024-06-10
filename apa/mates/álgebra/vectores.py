class Vector:
    """
    Clase usada para trabajar con vectores sencillos
    """
    def __init__(self, iterable):
        """
        Constructor de la clase Vector. Su único argumento es un iterable con las componentes del vector.
        """
        self.vector = [valor for valor in iterable]

    def __repr__(self):
        """
        Representación *oficial* del vector que permite construir uno nuevo idéntico mediante corta-y-pega.
        """
        return 'Vector(' + repr(self.vector) + ')'

    def __str__(self):
        """
        Representación *bonita* del vector.
        """
        return str(self.vector)

    def __getitem__(self, key):
        """
        Devuelve un elemento o una loncha del vector.
        """
        return self.vector[key]

    def __setitem__(self, key, value):
        """
        Fija el valor de una componente o loncha del vector.
        """
        self.vector[key] = value

    def __len__(self):
        """
        Devuelve la longitud del vector.
        """
        return len(self.vector)

    def __add__(self, other):
        """
        Suma al vector otro vector o una constante.
        """
        if isinstance(other, (int, float, complex)):
            return Vector(uno + other for uno in self)
        else:
            return Vector(uno + otro for uno, otro in zip(self, other))

    __radd__ = __add__

    def __neg__(self):
        """
        Invierte el signo del vector.
        """
        return Vector([-1 * item for item in self])

    def __sub__(self, other):
        """
        Resta al vector otro vector o una constante.
        """
        return -(-self + other)

    def __rsub__(self, other):
        """
        Método reflejado de la resta, usado cuando el primer elemento no pertenece a la clase Vector.
        """
        return -self + other

    def __mul__(self, other):
        """
        Retorna la multiplicación de un vector por un vector (elemento por elemento)
        """
        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Els vectors han de tenir la mateixa longitut")
            return Vector([self.vector[i] * other.vector[i] for i in range(len(self.vector))])
        elif isinstance(other, (int, float)):
            return Vector([other * value for value in self.vector])
        else:
            raise TypeError("No és possible multiplicar el vector per aquest objecte (ha de ser vector * vector)")

    def __rmul__(self, other):
        """
        Retorna la multiplicación de un vector por un escalar
        """
        if isinstance(other, (int, float)):
            return Vector([other * value for value in self.vector])
        else:
            raise TypeError("No és possible multiplicar el vector per aquest objecte (ha de ser vector * escalar)")

    def __matmul__(self, other):
        """
        Retorna el producto escalar de dos vectores
        """
        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Els vectors han de tenir la mateixa longitut")
            return sum([self.vector[i] * other.vector[i] for i in range(len(self.vector))])
        else:
            raise TypeError("No és possible multiplicar el vector per aquest objecte")

    __rmatmul__ = __matmul__

    def __floordiv__(self, other):
        """
        Retorna la componente tangencial
        """
        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Els vectors han de tenir la mateixa longitut")
            return ((self @ other)/(other @ other)) * other
        else:
            raise TypeError("No és possible multiplicar el vector per aquest objecte")

    __rfloordiv__ = __floordiv__

    def __mod__(self, other):
        """
        Retorna la componente normal
        """
        if isinstance(other, Vector):
            if len(self.vector) != len(other.vector):
                raise ValueError("Els vectors han de tenir la mateixa longitut")
            return self - (self // other)
        else:
            raise TypeError("No és possible calcular el mòdul del vector per aquest objecte")

    __rmod__ = __mod__

import doctest
doctest.testmod()
