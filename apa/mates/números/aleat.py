"""
Uso:
  aleat [--semilla=ENTERO] [--numero=ENTERO] [--norm] [--version]
  aleat -h | --help

Opciones:
  -s ENTERO --semilla=ENTERO    Semilla del generador de números aleatorios. [default: None]
  -n ENTERO --numero=ENTERO     Número de números aleatorios a generar. [default: 1]
  -N --norm                     Generar números reales normalizados en el rango 0 <= X < 1.
  -h --help                     Escribe la sinopsis en pantalla y finaliza la ejecución.
  --version                     Escribe el nombre del alumno y el año de realización y finaliza la ejecución.
"""

import sys
import apa
from docopt import docopt
from datetime import datetime as dt

def main():
    args = docopt(__doc__, version="aleat.py - Autor: [Tu Nombre] - 2024")
    
    seed = args['--semilla']
    if seed is None:
        seed = hash(dt.now())
    else:
        seed = int(seed)
    
    count = int(args['--numero'])
    normalized = args['--norm']
    
    if normalized:
        generator = apa.mates.números.aleat(m=2**31, a=1103515245, c=12345, x0=seed)
        for _ in range(count):
            print(next(generator) / 2**31)
    else:
        rand = apa.mates.números.Aleat(m=2**31, a=1103515245, c=12345, x0=seed)
        for _ in range(count):
            print(next(rand))

if __name__ == "__main__":
    main()

