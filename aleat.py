#! /usr/bin/env python

import sys
from docopt import docopt
from datetime import datetime as dt
from apa import Aleat

if __name__ == "__main__":
    usage = f""" 
    Gestión de números aleatorios

    Usage:
        {sys.argv[0]} --semilla=ENTERO | -s=ENTERO
        {sys.argv[0]} --numero=ENTERO | -n=ENTERO
        {sys.argv[0]} --norm | -N

    Options:
        --semilla=ENTERO, -s ENTERO   Si no se indica valor, el programa genera una semilla aleatoria
        --numero=ENTERO, -n ENTERO    Núm de números a generar. Por defecto, numero=1
        --norm, -N                    Si se indica -N, los valores se normalizaran en el rango 0<=x<=1
        --help, -h                    Muestra la sinopsis
        --version                     Finaliza la ejecución
    """
    arg = docopt(usage, help=True, version="Ona Bonastre Martí 2024")

    semilla = int(arg["--semilla"]) if arg["--semilla"] else hash(dt.now())
    aleatorios = Aleat(x0=semilla)

    num_to_generate = int(arg["--numero"]) if arg["--numero"] else 1
    vAleat = [next(aleatorios) for _ in range(num_to_generate)]
    
    vAleat = [n/max(vAleat) if arg["--norm"] else n for n in vAleat]

    for num in vAleat:
        print(num)