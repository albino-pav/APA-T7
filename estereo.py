#! /usr/bin/python3

import sys
from docopt import docopt 
from apa.audio.estereo import estereo2mono, mono2estereo

if __name__ == "__main__":
    usage = f"""
    
        WAV stereo a mono utilidades 
        
        Usage:
            {sys.argv[0]} mono [--left | --right | --suma | --diferencia] <ficEste> <ficMono>
            {sys.argv[0]} <ficIzq> <ficDer> <ficEste>
            {sys.argv[0]} <fic> <ficEste>
            {sys.argv[0]} -h | --help
            {sys.argv[0]} --version
        
        Options:
            -l, --left              Canal Izquierdo
            -r, --right             Canal Derecho
            -s, --suma              Suma los caanales [default]
            -d, --diferencial       Resta los canales
            -h, --help              Muestra ayuda
            --version               Muestra version
        
    """
    
    args = docopt(usage, help=True, version="0.01")
    
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
            
        estereo2mono(args["<ficEste>"], args["<ficMono>"], canal)
        
    else:
        
        mono2estereo(args["<ficIzq>"], args["<ficDer>"], args["<ficEste>"])





