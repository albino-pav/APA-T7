#! /usr/bin/env python3
import sys
from docopt import docopt
from datetime import datetime as dt
from apa.mates.números import Aleat

sinopsis = f"""
Generación de números aleatorios.

Usage:
    {sys.argv[0]} [--norm|-N] [--numero=<ENTERO>|-n <ENTERO>] [--semilla=<ENTERO>|-s <ENTERO>]
    {sys.argv[0]} -h | --help
    
Options:
    -s, --semilla=<ENTERO>          Establecer semilla del generador. 
    -n, --numero=ENTERO             Cantidad de números aleatorios a generar.
    -N, --norm                      Números decimales de 0 a 1.
    -h, --help                      Mostrar esta pantalla.
    --version                       Mostrar versión.
"""

if __name__ == "__main__":
    args = docopt(sinopsis, help=True, version="Yago Carballo 2024")
    
    numero = int(args["--numero"]) if args["--numero"] else 1
    semilla = int(args["--semilla"]) if args["--semilla"] else hash(dt.now())

    aleat = Aleat(x0=semilla)
    
    numNorm = aleat.x if args["--norm"] else 1
    
    for i in range(numero):
        print(f'#{i+1}: {next(aleat)/aleat.m if args["--norm"] else next(aleat)}')
    
        
    

    