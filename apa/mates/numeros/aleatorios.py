"""
Modulo para generar numeros aleatorios.
"""

class Aleat:
    """
    Generacion de numeros aleatorios
    """
    def __init__(self, *, m=2**48, a=25214903917, c=11, x0=1212121):
        self.m = m
        self.a = a 
        self.c = c
        self.x = x0
    
    def __next__(self):
        self.x = (self.a * self.x + self.c) % self.m
        return self.x
    
    def __iter__(self):
        return self
    
    def __call__(self, x0, /):
        self.x = x0


if __name__ == "__main__":
    import doctest
    doctest.testmod()
