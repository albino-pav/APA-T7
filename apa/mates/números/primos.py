

def esPrimo(numero):
    """
    Devuelve True si su argumento es primo, y False si no lo es.

    >>> [numero for numero in range(2, 50) if esPrimo(numero)]
    [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

    """
    if numero <= 1:
        return False
    elif numero <= 3:
        return True
    elif numero % 2 == 0 or numero % 3 == 0:
        return False
    for i in range(5, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True






def primos(numero):
    """
    Devuelve una tupla con todos los 
    números primos menores que su argumento.

    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)

    """
    primos_lista = []
    for num in range(2, numero):
        if esPrimo(num):
            primos_lista.append(num)
    return tuple(primos_lista)

def descompon(numero):
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.

    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)

    """
    factores_primos = []
    divisor = 2
    while numero > 1:
        while numero % divisor == 0:
            factores_primos.append(divisor)
            numero //= divisor
        divisor += 1
    return tuple(factores_primos)


#FUNCIONES PARA EL CÁLCULO DE MCM MCD

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    
    >>> mcm(90, 14)
    630

    """
    # Descomposición en factores primos de ambos números
    descomp_num1 = descompon(numero1)
    descomp_num2 = descompon(numero2)
    
    # Factores primos de ambos números
    factores_primos1 = list(descomp_num1)
    factores_primos2 = list(descomp_num2)

    # Eliminar los factores primos comunes entre ambos números
    for factor in descomp_num1:
        if factor in factores_primos2:
            factores_primos2.remove(factor)

    # Multiplicar los factores primos únicos de ambos números para obtener el MCM
    mcm = 1
    for factor in factores_primos1 + factores_primos2:
        mcm *= factor
    
    return mcm


def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de sus argumentos.
    
    >>> mcd(924, 780)
    12
    """
    # Descomposición en factores primos de ambos números
    descomp_num1 = descompon(numero1)
    descomp_num2 = list(descompon(numero2))  # Convertimos la tupla a una lista
    
    # Iteración factores primos de ambos números
    # para encontrar los factores comunes, el MCD
    mcd = 1
    for factor in descomp_num1:
        if factor in descomp_num2:
            mcd *= factor
            descomp_num2.remove(factor)  # Eliminamos el factor común de la lista de descomposición del segundo número
    
    return mcd


#Obtención del mínimo común múltiplo y el máximo común divisor para un número arbitrario de argumentos
def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de sus argumentos.
    
    >>> mcmN(42, 60, 70, 63)
    1260

    """
    # Inicializamos la variable para almacenar el MCM
    mcm = 1
    
    # Iteramos sobre todos los números dados
    for numero in numeros:
        # Calculamos el MCM entre el número actual y el MCM acumulado
        mcm = mcm * numero // mcd(mcm, numero)
    
    return mcm

def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de sus argumentos.
    
    >>> mcdN(840, 630, 1050, 1470)
    210

    """
    # Inicializamos la variable para almacenar el MCD
    resultado = numeros[0]
    
    # Iteramos sobre todos los números dados
    for numero in numeros[1:]:
        # Calculamos el MCD entre el número actual y el MCD acumulado
        while numero != 0:
            resultado, numero = numero, resultado % numero
    
    return resultado


import doctest

doctest.testmod(verbose=True)