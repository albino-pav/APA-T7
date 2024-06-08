#! /usr/bin/env python

import sys
from docopt import docopt
from apa import estereo2mono
from apa import mono2estereo

if __name__ == "__main__":
    usage = f""" 
    Manejo de ficheros WAVE mono y estéreo

    Usage:
        {sys.argv[0]} mono [options] <ficEste> <ficMono>
        {sys.argv[0]} <ficL> <ficR> <ficEste>
        {sys.argv[0]} <ficL> <ficEste>

    Options:
        --left, -l          La señal mono es el canal izquierdo de la señal estéreo
        --right, -r         La señal mono es el canar derecho de la señal estéreo
        --suma, -s          La señal mono es la semisuma de los dos canales de la señal estéreo
        --diferencia, -d    La señal mono es la semidiferencia de los dos canales de la señal estéreo
        --help, -h
        --version
    """
    arg = docopt(usage, help=True, version="Ona Bonastre Martí 2024")

    if arg["mono"]:
        if arg["--left"]:
            canal = 0
        elif arg["--right"]:
            canal = 1
        elif arg["--suma"]:
            canal = 2
        elif arg["--diferencia"]:
            canal = 3
        else:
            canal = 2
        try:
            estereo2mono(arg["<ficEste>"], arg["<ficMono>"], canal)
        except (ValueError, TypeError) as e:
            print(f"Error: {e}")

    else:
        if arg["<ficR>"]:
            try:
                mono2estereo(arg["<ficL>"], arg["<ficR>"], arg["<ficEste>"])
            except Exception as e:
                print(f"Se ha encontrado un error: {e}")
        else:
            try:
                mono2estereo(arg["<ficL>"], arg["<ficL>"], arg["<ficEste>"])
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")