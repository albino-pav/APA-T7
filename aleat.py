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
            -h, --help            Informacion de uso
            --version             Versiones
            -s, --semilla (INT)  Semilla para el generador de números aleatorios
            -n, --numero (INT)   Numero de números aleatorios a generar
            -N, --norm            Normalizar los números aleatorios entre 0 y 1
    """
    args = docopt(usage, help=True, version="Ivan Enciso Hernandez & Pau Codina Peñarroya 2024")
    
    seed = int(args["--semilla"]) if args["--semilla"] else hash(dt.now())
    n = int(args["--numero"]) if args["--numero"] else 1
    rand = Aleat(x0=seed)

    for _ in range(n):
        print(f"{next(rand) / rand.m if args['--norm'] else next(rand)}")
