#! /usr/bin/python3

import sys
from docopt import docopt
from datetime import datetime as dt
from apa.mates.numeros.aleatorios import *

if __name__ == "__main__":
    usage = f"""

        Generador numeros aleatorios
        
        Usage:
            {sys.argv[0]} [options]
        
        Options:
            -s, --semilla ENTERO    Semilla
            -n, --numero ENTERO     Numeros a generar
            -N, --norm              Normalizar numeros aleatorios
            -h, --help              Mostrar ayuda
            --version               Mostrar version
            
    """
    
    args = docopt(usage, help=True, version="0.01")
    
    if args["--semilla"]:
        seed = int(args["--semilla"])
    else:
        seed = hash(dt.now())
        
    rand = Aleat(x0=seed)
    
    if args["--numero"]:
        num = int(args["--numero"])
    else:
        num = 1
    
    for i in range(num):
        if args['--norm']:
            print(f"{next(rand) / rand.m}")
        else:
            print(f"{next(rand)}")
            
