from typing import Any

class Aleat:
    """
    Algrisme per la generació

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    """
    def __init__(self, *, m=32, a=9, c=13, x0=11): # m = 2**48, a = 25214903917, c = 11, x0 = 1212121):
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __next__(self):
        self.x = (self.x * self.a + self.c) % self.m
        return self.x
    
    def __iter__(self):
        return self
    
    def __call__(self, x0, /):
        self.x = x0


# if __name__ == "__main__":
#     import doctest
#     doctest.testmod(verbose=True)
