#! /usr/bin/python3

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


if __name__ == "__main__":
    import sys
    from docopt import docopt
    from datetime import datetime as dt
    usage = f"""
        Random number generator

        Usage:
            {sys.argv[0]} [options]
        
        Options:
            -h, --help            Usage information
            --version             Shows version
            -s, --semilla ENTERO  Seed of the number generator
            -n, --numero ENTERO   Number of random numbers to generate
            -N, --norm            Normalize the random numbers
    """
    args = docopt(usage, help=True, version="Gerard i Joel 2024")
    
    seed = int(args["--semilla"]) if args["--semilla"] else hash(dt.now())
    n = int(args["--numero"]) if args["--numero"] else 1
    rand = Aleat(x0=seed)

    for _ in range(n):
        print(f"{next(rand) / rand.m if args['--norm'] else next(rand)}")
