from docopt import docopt
import sys
import apa.audio.estereo as estereo
from apa.audio.estereo import estereo2mono, mono2estereo, codEstereo, decEstereo

__doc__="""
usage:
    estereo [Options] ficL [ficR] ficEste
    estereo mono [Options] ficEste ficMono
    estereo -h | --help
    estereo --versio
Options:
  -l, --left                   El senyal mono és el canal esquerre del senyal estèreo.
  -r, --right                  El senyal mono és el canal dret del senyal estèreo.
  -s, --sum                    El senyal mono és la semisuma dels dos canals del senyal estèreo.
  -d, --difference             El senyal mono és la semidiferència dels dos canals del senyal estèreo.
  -h, --help                   Escriu l'ajuda a la pantalla.
  --version                    Escriu el nom de l'alumne i l'any de realització.
"""

if __name__ == '__main__':
    args = docopt(__doc__, version='Gerard Soteras i Ferran Murcia, 2024')

    if args['estereo2mono']:
        estereo2mono(args['<ficEste>'], args['<ficMono>'], args['--canal'])
    elif args['mono2estereo']:
        mono2estereo(args['<ficIzq>'], args['<ficDer>'], args['<ficEste>'])
    elif args['codEstereo']:
        codEstereo(args['<ficEste>'], args['<ficCod>'])
    elif args['decEstereo']:
        decEstereo(args['<ficCod>'], args['<ficEste>'])