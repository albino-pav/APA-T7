#!/usr/bin/env python3

from docopt import docopt
import sys
from datetime import datetime as dt
from apa.mates.numeros.aleatorios import Aleat
__doc__="""
Generador de números aleatorios.

Usage:
  aleat [-s ENTERO] [-n ENTERO] [--norm]
  aleat -h | --help
  aleat --version

Options:
  -s, --semilla=<ENTERO>       Semilla del generador de números aleatorios. Si no se indica la opción, el programa generará una semilla aleatoria por sí mismo.
  -n,  --numero=<ENTERO>       Número de números aleatorios a generar. Por defecto, numero=1. Si se indica un número mayor, cada número aleatorio se escribirá en una línea separada.
  -N, --norm                   Por defecto, los números aleatorios generados son enteros. Si se indica la opción --norm, se escribirán reales, normalizados en el rango 0<=x<1.
  -h, --help                   Escribe la ayuda en pantalla y finaliza la ejecución.
  --version                    Escribe el nombre del alumno y el año de realización.
"""


if __name__ == '__main__':

    args = docopt(__doc__, version='Guillermo Efrén Medina Guamán y Raúl Gonzalez Díaz, 2024')
    
    semilla = int(args['--semilla']) if args['--semilla'] else hash(dt.now())
    numero = int(args['--numero']) if args['--numero'] else 1
    
    aleatori = Aleat(x0=semilla)
    
    normaux = args['--norm']

    for numeros in range(numero):
        value = next(aleatori)
        if normaux:
            value /= aleatori.m 
        print(f'aleatoris: {value}')
    