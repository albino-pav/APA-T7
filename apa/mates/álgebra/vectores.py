
import itertools as itt

class Vector:
    def __init__(self, iterable) -> None:
        self.vector = [it for it in iterable]

    def __str__(self):
        # return self.Vector.__str__()
        return str(self.vector)
    
    def __repr__(self):
        return 'Vector(' + str(self.vector) + ')'
    
    def __getitem__(self, key):
        return self.vector[key]
    
    def __setitem__(self, key, value):
        self.vector[key] = value
    
    def __len__(self):
        return len(self.vector)
    
    def __add__(self, otro):
        if isinstance(otro, (int, float, complex)):
            return Vector(a + otro for a in self)
        return Vector(a + b for a, b in itt.zip_longest(self,otro, fillvalue = ""))
    
    __radd__ = __add__

    def __neg__(self):
        return Vector(-a for a in self)
    
    def __sub__(self, otro):
        return self + (-otro)
    
    def __rsub__(self, otro):
        return (-self) + otro

    def __call__(self):
        # expresion for elemento in iterable if condicion
        return sum([i**2 for i in self])