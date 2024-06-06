
#!/usr/bin/env python3

import sys
from docopt import docopt
from datetime import datetime
from apa import Aleat

def main():
    doc = f"""
        Generador de numeros aleatorios

        Uso:
            {sys.argv[0]} [opciones]

        Opciones:
            -h, --help             Muestra esta ayuda
            --version              Muestra la version
            -s, --semilla ENTERO   Semilla para el generador
            -n, --cantidad ENTERO  Cantidad de numeros a generar
            -N, --normalizado      Normalizar los numeros generados
    """
    argumentos = docopt(doc, help=True, version="Version 2024")

    semilla = int(argumentos["--semilla"]) if argumentos["--semilla"] else int(datetime.now().timestamp())
    cantidad = int(argumentos["--cantidad"]) if argumentos["--cantidad"] else 1
    generador = Aleat(x0=semilla)

    for _ in range(cantidad):
        valor = next(generador)
        if argumentos["--normalizado"]:
            valor /= generador.m
        print(f"{valor}")

if __name__ == "__main__":
    main()


