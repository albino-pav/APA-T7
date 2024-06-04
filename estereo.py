#! /usr/bin/env python3
import sys
from docopt import docopt
from apa.audio import estereo


sinopsis = f"""

Tratamiento de ficheros WAV.

Usage:
    {sys.argv[0]} <ficL> [<ficR>] <ficEste>
    {sys.argv[0]} mono [options] <ficEste> <ficMono>
    {sys.argv[0]} -h | --help

Options:
    -l, --left          La señal mono en el canal izquierdo de la señal estéreo.
    -r, --right         La señal mono es el canal derecho de la señal estéreo.
    -s, --suma          La señal mono es la semisuma de los dos canales de la señal estéreo.
    -d, --diferencia    La señal mono es la semidiferencia de los dos canales de la señal estéreo.
    -h, --help          Muestra esta pantalla.
    --version           Muestra la versión.
"""

if __name__ == "__main__":
    args = docopt(sinopsis, help=True, version="Yago Carballo 2024")
    
    if args["mono"]:
        
        options = [args['--left'], args['--right'], args['--suma'], args['--diferencia']]

        if sum(bool(opt) for opt in options) > 1:
            raise ValueError("No debe contener más de una opción de estereofonía.")
        else:
            
            if args['--left']:
                opt = 0
            elif args['--right']:
                opt = 1
            elif args['--diferencia']:
                opt = 3
            else:
                opt = 2
            estereo.estereo2mono(args["<ficEste>"], args["<ficMono>"], opt)
    
    if args["<ficL>"]:
        estereo.mono2estereo(args["<ficL>"], args["<ficR>"] if args["<ficR>"] else args["<ficL>"], args["<ficEste>"])
    
        
        