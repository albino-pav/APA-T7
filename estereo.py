#!/usr/bin/env python3

import sys
from docopt import docopt
from apa.audio.estereo import *

def main():
    doc = f"""
            Gestion de archivos de audio WAVE

            Uso:
                {sys.argv[0]} mono [(--izquierda | --derecha | --suma | --diferencia)] <archivoEstereo> <archivoMono>
                {sys.argv[0]} <archivoIzquierdo> <archivoEstereo>
                {sys.argv[0]} <archivoIzquierdo> <archivoDerecho> <archivoEstereo>
                {sys.argv[0]} (-h | --help)
                {sys.argv[0]} --version

            Opciones:
                -h, --help             Muestra esta ayuda
                --version              Muestra la version
                -l, --izquierda        El audio mono es el canal izquierdo
                -r, --derecha          El audio mono es el canal derecho
                -s, --suma             El audio mono es la semisuma de ambos canales [por defecto]
                -d, --diferencia       El audio mono es la semidiferencia de ambos canales
        """
    argumentos = docopt(doc, help=True, version="Version 2024")
        
    if argumentos["mono"]:
            if argumentos["--izquierda"]:
                canal = 0
            elif argumentos["--derecha"]:
                canal = 1
            elif argumentos["--suma"]:
                canal = 2
            elif argumentos["--diferencia"]:
                canal = 3
            else:
                canal = 2

            try:
                estereo2mono(argumentos["<archivoEstereo>"], argumentos["<archivoMono>"], canal)
            except ValueError as e:
                print(f"Error: {e}")
    else:
            try:
                mono2estereo(
                    argumentos["<archivoIzquierdo>"], 
                    argumentos["<archivoDerecho>"] if argumentos["<archivoDerecho>"] else argumentos["<archivoIzquierdo>"],
                    argumentos["<archivoEstereo>"]
                )
            except ValueError as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
