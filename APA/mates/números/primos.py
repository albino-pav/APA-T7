"""
Sonia Sahuquillo Guillén y Marcel Farelo de la Orden
"""


def esPrimo(numero) -> bool:
    """
    Funció que retorna True si un número és primer 
    i False si no ho és.

    >>> [numero for numero in range(2, 50) if esPrimo(numero)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    """
    if numero <= 1:
        return False
    for value in range(2, int(numero**0.5) + 1):
        if numero % value == 0:
            return False
    return True
    

def primos(numero) -> tuple:
    """
    Retorna una tupla amb tots els nombres primers que es troben
    entre el 0 i el nombre escollit.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """
    return tuple(num for num in range(2, numero) if esPrimo(num))


def descompon(numero) -> tuple:
    """
    Retorna una tupla amb els factors primers del numero escollit.

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    tuple_ = []
    for valor in primos(numero):
        while numero % valor == 0:
            tuple_.append(valor)
            numero //= valor
    return tuple(tuple_)


def list_product(llista) -> int:
    """
    Retorna el producte de tots els elements d'una llista
    """
    producto = 1
    for factor in llista:
        producto *= factor
    return producto


def remove_same(llista1, llista2) -> list:
    """
    Retorna la llista2 sense els elements ja continguts a la llista1.
    """
    for factor in llista1:
        if factor in llista2:
            llista2.remove(factor)
    return llista2 


def same_factors(llista1, llista2) -> list:
    """
    Retorna una llista amb els elements que aparèixen tant a la llita1
    com a la llista2.
    """
    factores_comunes = []
    for factor in llista1:
        if factor in llista2:
            factores_comunes.append(factor)
            llista2.remove(factor)
    return factores_comunes


def mcm(numero1, numero2) -> int:
    """
    Retorna el mínin comú múltiple dels números 1 i 2.

    >>> mcm(90, 14)
    630
    """
    factores_primos_num1 = list(descompon(numero1))
    factores_primos_num2 = list(descompon(numero2))
  
    factores_mcm = (factores_primos_num1 
                    + remove_same(factores_primos_num1, factores_primos_num2))
    return list_product(factores_mcm)


def mcd(numero1, numero2) -> int:
    """
    Retorna el màxim comú divisor dels números 1 i 2.

    >>> mcd(924, 780)
    12
    """
    factores_primos_num1 = list(descompon(numero1))
    factores_primos_num2 = list(descompon(numero2))
    return list_product(same_factors(factores_primos_num1, 
                                     factores_primos_num2))


def mcmN(*argumentos) -> int:
    """
    Retorna el mínim comú múltiple dels arguments donats.

    >>> mcmN(42, 60, 70, 63)
    1260
    """
    factores_mcm = []
    for num in argumentos:
        factores_mcm += remove_same(factores_mcm, list(descompon(num)))

    return list_product(factores_mcm)


def mcdN(*argumentos) -> int:
    """
    Retorna el màxim comú divisor dels arguments donats.

    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    factores_mcd = list(descompon(argumentos[0]))
    for num in argumentos:
        factores_num = list(descompon(num))
        factores_mcd = same_factors(factores_mcd, factores_num)
    
    return list_product(factores_mcd)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
