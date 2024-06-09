#!/usr/bin/env python3

from docopt import docopt
from datetime import datetime as dt
import random

__doc__ = """
usage:
    aleat [--semilla=ENTERO] [--numero=ENTERO] [--norm] [--help] [--version]

Options:
    --semilla=ENTERO, -s ENTERO  Llavor per a la generació de números aleatoris
    --numero=ENTERO, -n ENTERO   Número de números aleatoris a generar
    --norm, -N                   Generar numeros aleatoris en el rang [0, 1).
    --help, -h                   Mostra ajuda
    --version                    Motra el nom del alumne i l'any de realització.
"""



def aleat(args):
    # Establecer la semilla
    if args['--semilla']:
        random.seed(int(args['--semilla']))
    else:
        random.seed(hash(dt.now()))

    # Generar números aleatorios
    for _ in range(int(args['--numero'])):
        if args['--norm']:
            print(random.random())  # Generar un número aleatorio en el rango [0, 1)
        else:
            print(random.randint(0, 100))  # Generar un número entero aleatorio

if __name__ == '__main__':
    arguments = docopt(__doc__, version='Gerard Soteras i Ferran Murcia, 2024')
    aleat(arguments)