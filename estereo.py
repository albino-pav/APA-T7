#! /usr/bin/python3

import sys
from docopt import docopt
from apa import estereo2mono, mono2estereo

if __name__ == "__main__":
    usage = f"""
        WAVE audio files management

        Usage:
            {sys.argv[0]} mono [(--left | --right | --suma | --diferencia)] <ficEste> <ficMono>
            {sys.argv[0]} <ficL> <ficEste>
            {sys.argv[0]} <ficL> <ficR> <ficEste>
            {sys.argv[0]} (-h | --help)
            {sys.argv[0]} --version

        Options:
            -h, --help            Informacion
            --version             Versiones
            -l, --left            Canal izquiedo es mono
            -r, --right           canal derecho es mono
            -s, --suma            semi-suma de ambos canales (default)
            -d, --diferencia      semi-diferencia de ambos canales
    """
    args = docopt(usage, help=True, version="Ivan Enciso Hernandez & Pau Codina Peñarroya 2024")
    
    if args["mono"]:
        if args["--left"]:
            canal = 0
        elif args["--right"]:
            canal = 1
        elif args["--suma"]:
            canal = 2
        elif args["--diferencia"]:
            canal = 3
        else:
            canal = 2

        try:
            estereo2mono(args["<ficEste>"], args["<ficMono>"], canal)
        except ValueError as e:
            print(e)
    else:
        try:
            mono2estereo(
                args["<ficL>"], 
                args["<ficR>"] if args["<ficR>"] else args["<ficL>"],
                args["<ficEste>"])
        except ValueError as e:
            print(e)