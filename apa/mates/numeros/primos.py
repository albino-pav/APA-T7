"""
Funciones de primos
"""

def esPrimo(numero):
    """
    torna si el número és primer o no
    >>> [numero for numero in range(2, 50) if esPrimo(numero)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    """

    return numero > 1 and all(numero % n != 0 for n in range(2,numero))

def primos(numero):
    """
    torna els nombres primers menors que l'argument
    >>> primos (50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """

    primos_encontrados = [n for n in range(2, numero) if esPrimo(n)]
    return tuple(primos_encontrados)

# def descompon(numero):
#     factores = []
#     for primo in primos(numero):
#         while numero % primo == 0:
#             factores.append(primo)
#             numero //= primo
#     return tuple(factores)

def descompon(numero):
    """
    torna la descomposició en nombres primers de l'argument
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """

    factores = []
    divisor = 2
    while numero > 1:
        if numero % divisor == 0 and esPrimo(divisor):
            factores.append(divisor)
            numero //= divisor
        else:
            divisor += 1
    return tuple(factores)

def mcm(numero1, numero2):
    """
    torna el mínim comú múltiple de dos nombres
    >>> mcm(90, 14)
    630
    """

    factores_numero1 = descompon(numero1)
    factores_numero2 = descompon(numero2)

    factores_comunes = set(factores_numero1) | set(factores_numero2)

    mcm_resultado = 1
    
    for factor in factores_comunes:
        exponente = max(factores_numero1.count(factor), factores_numero2.count(factor))
        mcm_resultado *= factor ** exponente
    
    return mcm_resultado

def mcd(numero1, numero2):
    """
    torna el màxim comú divisor de dos nombres
    >>> mcd(924, 780)
    12
    """

    factores_numero1 = descompon(numero1)
    factores_numero2 = descompon(numero2)
    
    factores_comunes = set(factores_numero1) & set(factores_numero2)
    
    mcd_resultado = 1
    
    for factor in factores_comunes:
        exponente = min(factores_numero1.count(factor), factores_numero2.count(factor))
        mcd_resultado *= factor ** exponente
    
    return mcd_resultado

def mcmN(*numeros):
    """
    torna el mínim coú múltiple de tants nombres com es passin a l'argument
    >>> mcmN(42, 60, 70, 63)
    1260
    """

    factores_numeros = [descompon(num) for num in numeros]
    
    factores_comunes = set()

    for tupla in factores_numeros:
        factores_comunes.update(tupla)

    max_exponentes = {}
    for factor in factores_comunes:
        max_exponentes[factor] = max(tupla.count(factor) for tupla in factores_numeros)

    mcm_resultado = 1
    for factor, exponente in max_exponentes.items():
        mcm_resultado *= factor ** exponente

    return mcm_resultado

def mcdN(*numeros):
    """
    torna el màxim comú divisor de dos nombres
    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    
    factores_numeros = [descompon(num) for num in numeros]
    
    factores_comunes = set()

    for tupla in factores_numeros:
        factores_comunes.update(tupla)

    min_exponentes = {}
    for factor in factores_comunes:
        min_exponentes[factor] = min(tupla.count(factor) for tupla in factores_numeros)

    mcd_resultado = 1
    for factor, exponente in min_exponentes.items():
        mcd_resultado *= factor ** exponente

    return mcd_resultado