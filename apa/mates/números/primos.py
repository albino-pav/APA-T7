#!/usr/bin/env python3

"""
    Determinación de la primalidad y mínimo común múltiplo y máximo común divisor
"""

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo, y False si no lo es.
    >>> esPrimo(13)
    True
    """
    if numero <= 1: 
        return False

    for i in range(2,int(numero**0.5) + 1):
        if numero%i == 0:
            return False
    return True

def primos(numero):
    """
    Devuelve una tupla con todos los números primos menores que su argumento.
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    
    if numero <= 1: 
        return False
    
    return tuple([i for i in range(2,numero) if esPrimo(i)])


def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.  
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """

    if esPrimo(numero):
        return (numero, )

    lista = []
    for i in primos(numero):
        while numero % i == 0:
            lista.append(i)
            numero /= i
            
    return tuple(lista)

def mcm(a, b):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcm(90, 14)
    630
    """
    factores_a = list(descompon(a))
    factores_b = list(descompon(b))

    mcm = 1
    i,j = 0, 0

    for i in factores_a:
        if i in factores_b:
            mcm *= i
            factores_b.remove(i)
        else:
            mcm *= i


    for i in factores_b:
        mcm *= i

    return mcm


def mcd(a, b): 
    """
    Devuelve el máximo común divisor de sus argumentos.
    >>> mcd(924, 780)
    12
    """
    factores_a = list(descompon(a))
    factores_b = list(descompon(b))

    mcd = 1

    for i in factores_a:
        if i in factores_b:
            factores_b.remove(i)
            mcd *= i
    
    return mcd

def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    >>> mcmN(42, 60, 70, 63)
    1260
    """
    acumulado = numeros[0]

    for numero in numeros[1:]:
        acumulado = mcm(acumulado,numero)

    return acumulado

def mcdN(*numeros): 
    """
    Devuelve el máximo común divisor de sus argumentos.
    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    acumulado = numeros[0]

    for numero in numeros[1:]:
        acumulado = mcd(acumulado,numero)

    return acumulado

if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=True)

    import sys
    from docopt import docopt

    sinopsis = f"""
    Calcula los numeros primos de cierto valor.
    
    Usage:
        {sys.argv[0]} primos <valor_maximo>
        {sys.argv[0]} descompon <valor>
        {sys.argv[0]} esPrimo [-n|--numeric] <valor> 
        {sys.argv[0]} mcm <valores> ...
        {sys.argv[0]} -h | --help
    
    Options:
        -n, --numeric  Muestra el resultado de esPrimo de manera numérica.
    """
    args = docopt(sinopsis)
    if args["primos"]:
        numero = int(args["<valor_maximo>"])
        print(f"{primos(numero)}")
    elif args["esPrimo"]:
        numero = int(args["<valor>"])
        if args["--numeric"]: # Siempre la opcion larga
            print(f"{1 if esPrimo(numero) else 0}")
        else:
            print(f"{esPrimo(numero)}")
    elif args["mcm"]:
        numeros = [int(numero) for numero in args["<valores>"]]
        print(f"{mcmN(*numeros) = }")
    else:
        numero = int(args["<valor>"])
        print(f"{descompon(numero) = }")
