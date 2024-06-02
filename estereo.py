
import sys
from docopt import docopt 
from apa.audio import estereo2mono, mono2estereo

if __name__ == "__main__":
    usage = f"""
    
        WAVE file manager
        
        Usage:
            {sys.argv[0]} mono [--left | --right | --suma | --difrencia] <ficEste> <ficMono>
            {sys.argv[0]} <ficL> <ficR> <ficEste>
            {sys.argv[0]} <fic> <ficEste>
            {sys.argv[0]} -h | --help
            {sys.argv[0]} --version
        
        Options:
            -l, --left              Left channel
            -r, --right             Right channel
            -s, --suma              Sum of both channels [default]
            -d, --difrencial        Difference between both channels
            -h, --help              Shows information about the program
            --version               Shows version
        
    """
    
    args = docopt(usage, help=True, version="Pol Raich | 2024")
    
    if args["mono"]:
        if args["--left"]:
            canal = 0
            
        elif args["--right"]:
            canal = 1
            
        elif args["--suma"]:
            canal = 2
            
        elif args["--difrencia"]:
            canal = 3
            
        else:
            canal = 2
            
        estereo2mono(args["<ficEste>"], args["<ficMono>"], canal)
        
    else:
        mono2estereo(args["<ficL>"], args["<ficR>"] if args["<ficR>"] else args["<ficL>"], args["<ficEste>"])