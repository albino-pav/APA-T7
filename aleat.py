#! /usr/bin/python3

import sys
from docopt import docopt
from datetime import datetime as dt
from apa.mates.números.aleatorios import *

if __name__ == "__main__":
    usage = f"""

        Random number generator
        
        Usage:
            {sys.argv[0]} [options]
        
        Options:
            -s, --semilla ENTERO    Radom number generator seed
            -n, --numero ENTERO     Numbers to generate
            -N, --norm              Normalize generated numbers
            -h, --help              Shows information about the program
            --version               Shows version
            
    """
    
    args = docopt(usage, help=True, version="Pol Raich | 2024")
    
    seed = int(args["--semilla"]) if args["--semilla"] else hash(dt.now())
    rand = Aleat(x0=seed)
    
    for i in range(int(args["--numero"]) if args["--numero"] else 1):
        print(f"{next(rand) / rand.m if args['--norm'] else next(rand)}")
    