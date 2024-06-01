#! /usr/bin/python3

import sys
from docopt import docopt
from datetime import datetime as dt
from apa import Aleat

if __name__ == "__main__":
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
