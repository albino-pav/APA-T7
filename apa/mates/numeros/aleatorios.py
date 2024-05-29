#! /usr/bin/python3

import sys
from docopt import docopt 

class Aleat:
    """
    Aleat class to generate random variables

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

sinposis = f"""
    Aleat.

    Usage:
        {sys.argv[0]} [options]
    
    Options:
        -h --help                Usage information
        -v --version             Shows version
        -s --semilla=<entero>    Seed of the number generator
"""

if __name__ == "__main__":
    args = docopt(sinposis, help=True, version="Aleat v1.0")
    if args["-n"]

