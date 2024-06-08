#!/usr/bin/env python3

from docopt import docopt
import sys
import apa.audio.estereo as estereo
from apa.audio.estereo import estereo2mono, mono2estereo, codEstereo, decEstereo

__doc__="""
Usage:
    estereo [opciones] ficL [ficR] ficEste
    estereo mono [opciones] ficEste ficMono
    estereo -h | --help
    estereo --version
Options:
  -l, --left                   La señal mono es el canal izquierdo de la señal estéreo.
  -r, --right                  La señal mono es el canal derecho de la señal estéreo.
  -s, --suma                   La señal mono es la semisuma de los dos canales de la señal estéreo.
  -d, --diferencia             La señal mono es la semidiferencia de los dos canales de la señal estéreo.
  -h, --help                   Escribe la ayuda en pantalla.
  --version                    Escribe el nombre del alumno y el año de realización.
"""

if __name__ == '__main__':
    args = docopt(__doc__, version='Guillermo Efrén Medina Guamán y Raúl Gonzalez Díaz, 2024')

    if args['estereo2mono']:
        estereo2mono(args['<ficEste>'], args['<ficMono>'], args['--canal'])
    elif args['mono2estereo']:
        mono2estereo(args['<ficIzq>'], args['<ficDer>'], args['<ficEste>'])
    elif args['codEstereo']:
        codEstereo(args['<ficEste>'], args['<ficCod>'])
    elif args['decEstereo']:
        decEstereo(args['<ficCod>'], args['<ficEste>'])



