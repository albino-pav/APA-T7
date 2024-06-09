"""
Módulo con funciones para el manejo de números primos.

Autores: Ivan Enciso & Pau Codina

Fecha: 2023-11-15
"""

def esPrimo(numero):
  """
  Descripcion:
    Comprueba si un numero es primo o no.

  Parametros:
    Variable int a comprobar.

  Salida:
    Variable boleana, Tue si es primo, False en caso contrario.
  """
  if numero <=1:
    return False
  for prueba in range(2, int(numero**0.5) + 1):  #Unicamente comprobamos hata la raiz cuadrada de numero.
    if numero % prueba == 0:
      return False
  return True

def primos(numero):
  """
  Descripcion:
    Devuelve una tupla con todos los numeros menores que numero.
  Parametros:
    Variable que intica el limite superior para la generacion de primos.
  Salida:
    Tupla de numeros primos hasta numero.
  """
  primos = []
  for prueba in range (2, numero):
    if esPrimo(prueba):
      primos.append(prueba)
  return tuple(primos)

def descompon(numero):
  """
  Descripcion:
    Devuelve una tupla con la descomposicion en factores primos de numero.
  Parameteos:
    Variable entera a descomponer en factores primos.
  Salida:
    Tupla con la decomposicion en factores primos de numero.
  """
  factores = []

  while numero % 2 == 0:
    factores.append(2)
    numero //=2

  for prueba in range(3, int(numero ** 0.5)+1, 2):
    factores.append(prueba)
    numero //= prueba
  
  if numero > 2:
    factores.append(numero)

  return factores

def mcm(numero1, numero2): 
  """
  Descipcion:
    Devuelve el mínimo común múltiplo de sus argumentos.
  Parametros:
    Numero1 (int): El primer número.
    Numero2 (int): El segundo número.
  Salida:
    El máximo común divisor de numero1 y numero2.
  """
  descomposicion1 = descompon(numero1)
  descomposicion2 = descompon(numero2)
  mcmFactores = []

  return mcmFactores

def mcd(numero1, numero2): 
  """
  Descipcion:
    Devuelve el máximo común divisor de sus argumentos.
  Parametros:
    numero1 (int): El primer número.
    numero2 (int): El segundo número.
  Salida:
    El mínimo común múltiplo de numero1 y numero2
  """
  descomposicion1 = descompon(numero1)
  descomposicion2 = descompon(numero2)
  mcdFactores = []

  return mcdFactores

def mcmN(*numeros):
    """
    Descipcion:
      Calcula el mínimo común múltiplo de un número arbitrario de argumentos.
    Parametros:
      *numeros (int): Números de los que se calculará el mínimo común múltiplo.
    Salida:
      int: Mínimo común múltiplo de los números dados.
    """
    mcm_resultado = 1
    for num in numeros:
        mcm_resultado = mcm(mcm_resultado, num)
    return mcm_resultado

def mcdN(*numeros):
    """
    Descipcion:
      Calcula el máximo común divisor de un número arbitrario de argumentos.
    Parametros:
      *numeros (int): Números de los que se calculará el máximo común divisor.
    Salida:
      int: Máximo común divisor de los números dados.        
    """
    mcd_resultado = numeros[0]
    for num in numeros[1:]:
        mcd_resultado = mcd(mcd_resultado, num)
    return mcd_resultado

if __name__ == "__main__":
    import doctest
    doctest.testmod()