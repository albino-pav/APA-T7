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
            -h, --help            Usage information
            --version             Shows version
            -l, --left            Mono audio is the left channel
            -r, --right           Mono audio is the right channel
            -s, --suma            Mono audio is the semi-sum of both channels [default]
            -d, --diferencia      Mono audio is the semi-difference of both channels
    """
    args = docopt(usage, help=True, version="Gerard i Joel 2024")
    
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
