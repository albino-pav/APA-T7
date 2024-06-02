#! /usr/bin/python3

"""
Alumnos: Víctor Pallàs i Pol Raich
"""


import math


def esPrimo(num):
    """
    Devuelve True si su argumento es primo y False si no lo es
    >>> [ numero for numero in range(2, 50) if esPrimo(numero) ]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """
    
    for it in range(2, num):
        if num % it == 0: 
            return False      
    return True


def primos(lim):
    """
    Devuelve una tupla de todos los primos hasta el argumento sin incluirlo
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    
    return tuple(i for i in range(2, lim) if esPrimo(i))


def descompon(num):
    """
    Devuelve una tupla con la descomposición en números primos del argumento ordenada de menor a mayor
    En este caso utilizamos La Propiedad de los número primos donde si un numero compuesto n tiene un divisor d, d <= sqrt(n)
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """   
     
    desc = []
    divisor = 2    
    while divisor * divisor <= num:
        if num % divisor == 0:
            desc.append(divisor)
            num //= divisor
        else:
            divisor += 1    
    if num > 1:
        desc.append(num)    
    return tuple(desc)


def mcm(num1, num2):
    """
    Devuelve el mínimo común múltiplo de los dos argumentos
    >>> mcm(90, 14)
    630
    """
    
    desc1 = descompon(num1)
    desc2 = descompon(num2)
    mCmList = list(desc1)
    for i in range(len(desc2)):
        quantInDesc1 = mCmList.count(desc2[i])
        quantInDesc2 = desc2.count(desc2[i])
        if quantInDesc1 < quantInDesc2:
            n = quantInDesc2 - quantInDesc1
            for j in range(n):
                mCmList.append(desc2[i])       
    return math.prod(mCmList)


def mcd(num1, num2):
    """Devuelve el máximo común divisor de los dos argumentos.
    Utilizando la propiedad: mcd(a, b) = a * b / mcm(a, b)
    >>> mcd(924, 780)
    12
    """
    
    return num1 * num2 // mcm(num1, num2)


def mcmN(*nums):
    """Devuelve el mínimo común múltiplo de todos los argumentos
    >>> mcmN(42, 60, 70, 63)
    1260
    """
    
    MCM = 1
    for i in range(len(nums)):
        MCM = mcm(MCM, nums[i])
    return MCM


def mcdN(*nums):
    """
    Devuelve el máximo común divisor de todos los argumentos
    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    
    MCD = nums[0]
    for num in nums[1: ]:
        MCD = mcd(MCD, num)
    return MCD
    

if __name__ == "__main__":
    # import doctest
    # doctest.testmod(verbose=True)
    import sys
    from docopt import docopt
    
    # [] -> Opcional
    # <> -> Variable obligatoria
    
    usage = f"""
        Manejo de numeros primos
        
        Usage:
            {sys.argv[0]} primos <valor_maximo>
            {sys.argv[0]} primos <valor_maximo>
            {sys.argv[0]} esPrimo [-n|--numero] <numero>
            {sys.argv[0]} mcm <numero> ...
            {sys.argv[0]} -h | --help
            
        Options:
            -n, --numeric  Devuelve 1 si el numero es primo y 0 si no lo es.
    """
    
    args = docopt(usage)
    if args["primos"]:
        
        numero = int(args["<valor_maximo>"]) 
        print(f"{primos(numero)}")
    
    elif args["esPrimo"]:
        numero = int(args["<numero>"])
        if args["--numero"]: #Siempre la opcion larga
            print(f"{1 if esPrimo(numero) else 0}")
        
    elif args["mcm"]:
        numeros = [int(num) for num in args["<numero>"]]
        print(f"{mcmN(*numeros)}")
    
    else :
        numero = int(args["<numero>"])
        print(f"{descompon(numero) = }")