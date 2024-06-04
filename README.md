# Paquetes y Programas (versión provisional)

## Nom i cognoms: Yago Carballo Barros

## Fecha de entrega: 9 de junio a medianoche

## Creación del paquete `apa`

Debe crearse un paquete que incluya las funciones desarrolladas durante el curso y que tenga la siguiente estructura:

```text
    apa
    ├── análisis
    │   └── horas.py
    ├── audio
    │   └── estereo.py
    └── mates
        ├── álgebra
        │   └── vectores.py
        └── números
            ├── aleatorios.py
            └── primos.py
```

El paquete debe ser plenamente operativo como un paquete estándar de Python. Es decir, deben escribirse los
distintos ficheros `__init__.py` de manera que se pueda acceder a todas las definiciones del paquete ejecutando
la orden `import apa`.

Algunos otros ejemplos de importación que deben permitirse se detallan en la tabla siguiente:

| Comando de importación            | Ejemplos de algunos objetos importados |
| --------------------------------- | -------------------------------------- |
| `import apa`                      | `apa.análisis.normalizaHoras()`        |
|                                   | `apa.mates.álgebra.Vector`             |
| `from apa import *`               | `análisis.normalizaHoras()`            |
|                                   | `mates.números.mcm()`                  |
| `from apa.mates import *`         | `álgebra.Vector`                       |
|                                   | `números.Aleat`                        |
| `from apa.mates.números import *` | `descompon()`                          |
|                                   | `mcm()`                                |

## Conversión a programa de `aleat()` y `estereo.py`

Deben construirse los programas que permitan acceder a las funciones de generación de números aleatorios
de `aleat.py` y de gestión de señales de audio y estéreo de `estereo.py`. En ambos casos, las funciones
empleadas deben **importarse** del paquete `apa` construido en el apartado anterior, y deberá usarse la
biblioteca `docopt` para gestionar el mensaje de sinopsis y las opciones y argumentos del programa.

### Gestión de números aleatorios

Debe escribirse el programa `aleat` que escribirá en pantalla uno o más números aleatorios con las
siguientes opciones:

| Opción                        | Descripción                                                             |
| ----------------------------- | ----------------------------------------------------------------------- |
| `--semilla=ENTERO, -s ENTERO` | Semilla del generador de números aleatorios. Si no se indica la opción, |
|                               | el programa generará una semilla aleatoria por sí mismo.                |

> NOTA: un modo habitual de conseguir números (casi) completamente aleatorios es aleatorizando la fecha
> y hora de la llamada. Por ejemplo, con la orden siguiente:
>
> ```python
>  from datetime import datetime as dt
>  
>  semilla = hash(dt.now())
> ```

| Opción                       | Descripción                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------- |
| `--numero=ENTERO, -n ENTERO` | Número de números aleatorios a generar. Por defecto, `numero=1`. Si se indica |
|                              | un número mayor, cada número aleatorio se escribirá en una línea separada.    |
| `--norm, -N`                 | Por defecto, los números aleatorios generados son enteros. Si se indica la    |
|                              | opción `--norm`, se escribirán reales, normalizados en el rango $0\le x<1$.   |
| `--help, -h`                 | Escribe la sinopsis en pantalla y finaliza la ejecución.                      |
| `--version`                  | Escribe el nombre del alumno y el año de realización y finaliza la ejecución. |

Las opciones `--help` y `--version` deben ser gestionadas directamente por `docopt`.

### Manejo de ficheros WAVE mono y estéreo

Se escribirá el programa `estereo` que tendrá dos modos de funcionamiento; si se indica el comando
`mono`, realizará la conversión de una señal estéreo a mono; si no se indica, se forma una señal
estéreo a partir de las señales contenidas en uno o dos ficheros mono:

```console
usuario:~/APAV$ estereo [opciones] ficL [ficR] ficEste     # mono -> estéreo
usuario:~/APAV$ estereo mono [opciones] ficEste ficMono    # estéreo -> mono
```

En el modo por defecto, sin el comando `mono`, la señal estéreo se puede formar a partir de dos
señales mono, que se corresponden con el canal izquierdo y derecho, o con sólo uno, que se duplicará en
los dos canales de la señal estéreo. No se admite más opciones que `--help`, que mostrará la sinopsis
del programa, y `--version`, que mostrará el nombre de alumno y el año de realización. Ambas opciones
deberán ser gestionadas por `docopt`.

En el modo `mono`, además de `--help` y `--version`, se permiten las siguientes opciones,
***mutuamente excluyentes***:

| Opción                        | Descripción                                                                |
| ----------------------------- | -------------------------------------------------------------------------- |
| `--left, -l`                  | La señal mono es el canal izquierdo de la señal estéreo.                   |
| `--right, -r`                 | La señal mono es el canal derecho de la señal estéreo.                     |
| `--suma, -s`                  | La señal mono es la semisuma de los dos canales de la señal estéreo.       |
| `--diferencia, -d`            | La señal mono es la semidiferencia de los dos canales de la señal estéreo. |

Por defecto, la señal mono se construye mediante semisuma de los dos canales (opción `--suma`).

El programa debe finalizar con un mensaje explicativo del error cometido si se cumplen una de estas dos
situaciones:

- Invocación incorrecta, con opciones o argumentos incorrectos o incompatibles entre sí. Por ejemplo, usar las
  opciones del modo `mono` en el modo estándar o usar más de una opción en aquél.

  Esta situación **debe** ser gestionada por `docopt`.

- Si alguno de los ficheros de entrada no responde al formato adecuado. Por ejemplo, si el fichero de entrada
  en el modo `mono` ya es mono.

  Esta situación debe gestionarse desde el programa y el mensaje mostrado en pantalla debe explicar con
  claridad el motivo del error.

## Entrega

Deberá subirse al repositorio GitHub el directorio del paquete `apa` y los dos programas `aleat` y `estereo`,
que deberán ser ejecutables directamente desde la línea de comandos de Linux (permisos de ejecución y
*hashbang* adecuados).
