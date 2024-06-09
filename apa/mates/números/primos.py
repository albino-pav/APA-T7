def esPrimo(numero):
    
    """
    devuelve True si el numero es primo y False si no lo es
    
    >>> for numero in range (2, 50):
    ...    if esPrimo(numero):
    ...        print(numero)
    2
    3
    5
    7
    11
    13
    17
    19
    23
    29
    31
    37
    41
    43
    47
    """
    for prueba in range (2, numero):
        if numero % prueba == 0:
            return False
    else: return True   

def primos(numero):
    
    """
    devuelve una tupla con todos los numeros primos menores
    
    >>> primos(50)
    (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
    """ 
    return tuple(prueba for prueba in range(2, numero) if esPrimo(prueba))

def descompon(numero):                          #Devuelve una tupla con la descomposición en factores primos de su argumento.
    
    """
    Devuelve una tupla con la descomposición en factores primos de su argumento.
    
    >>> descompon(36 * 175 * 143)
    (2, 2, 3, 3, 5, 5, 7, 11, 13)
    """
    factores_primos = []                        #crea una llista buida
    divisor = 2                                 #divizor iinicialitzat a 2 
    while numero > 1:                           #mentre numero sigui mes gran que 1
        if numero % divisor == 0:               #si el residu de la divisio de numero i divisor es 0
            factores_primos.append(divisor)     #afegeix divisor a la llista
            numero = numero / divisor           #numero es igual a la divisio de numero i divisor 
        else:
            divisor += 1                        #si no es compleix la condicio anterior incrementa el divisor en 1
    return tuple(factores_primos)               #retorna la llista passada a tupla amb els factors primers

def mcm(numero1, numero2):
    """
    Devuelve el mínimo común múltiplo de dos números enteros.
    
    Hem utilitzat el metode de descomposició en factors primers per aconseguir el mcm de dos numeros enters.
    
    >>> mcm(90, 14)
    630
    """
    factores_primos1 = descompon(numero1) #
    factores_primos2 = descompon(numero2)
    factores_comunes = []
    factores_no_comunes = []
    mcm = 1
    
    factores_comunes = list(set(factores_primos1) & set(factores_primos2)) #trobem els factors comuns no repetits (gracies el set que borra repetits)
    factores_no_comunes = list(set(factores_primos1) ^ set(factores_primos2)) #trobem els factors no comuns no repetits (gracies el set que borra repetits)
    
    # a continuació recorrem els factors comuns i comptem quants cops es repeteixen en cada llista de factors primers, el que és repeteixi més vegades es multiplica al mcm
            
    for factor in factores_comunes:
        mcm *= factor ** max(factores_primos1.count(factor), factores_primos2.count(factor))
    
    #ara recorrem els factors no comuns i els multipliquem al mcm elevats al nombre de vegades que es repeteixen 
            
    for factor in  factores_no_comunes:
        if factor in factores_primos1:
            mcm *= factor ** factores_primos1.count(factor)
        else: 
            mcm *= factor ** factores_primos2.count(factor)       
    return mcm

def mcd(numero1, numero2):
    """
    Devuelve el máximo común divisor de dos números enteros.
    
    Utiliza la descomposición en factores primos para obtener el mcd de dos números enteros.
        
    >>> mcd(924, 780)
    12
    """
    factores_primos1 = descompon(numero1)
    factores_primos2 = descompon(numero2)
    factores_comunes = list(set(factores_primos1) & set(factores_primos2))
    mcd = 1
        
    for factor in factores_comunes:
        mcd *= factor ** min(factores_primos1.count(factor), factores_primos2.count(factor))
        
    return mcd

def mcmN(*numeros):
    """
    Devuelve el mínimo común múltiplo de un numero arbitrario de numeros. 
    
    >>> mcmN(42, 60, 70, 63)
    1260
    """
    mcm_total = 1
    for numero in numeros:
        mcm_total = mcm(mcm_total, numero) #encontramos el mcm comun de todos los numeros
    return mcm_total

def mcdN(*numeros):
    """
    Devuelve el máximo común divisor de un numero arbitrario de numeros. 
    
    >>> mcdN(840, 630, 1050, 1470)
    210
    """
    mcd_total = numeros[0] #inicializamos el mcd_total al primer numero de la lista de numeros passados a la funcion 
    for numero in numeros:
        mcd_total = mcd(mcd_total, numero) #encontramos el mcd comun de todos los numeros
    return mcd_total

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)    
    