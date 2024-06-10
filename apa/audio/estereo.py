import struct
import sys
from docopt import docopt

# Definición de la interfaz del programa usando docopt
doc = """
Uso:
  estereo [opciones] ficL [ficR] ficEste
  estereo mono [opciones] ficEste ficMono

Opciones:
  -h --help       Muestra este mensaje de ayuda.
  -v --version    Muestra la versión del programa.
  -l --left       La señal mono es el canal izquierdo de la señal estéreo.
  -r --right      La señal mono es el canal derecho de la señal estéreo.
  -s --suma       La señal mono es la semisuma de los dos canales de la señal estéreo.
  -d --diferencia La señal mono es la semidiferencia de los dos canales de la señal estéreo.
"""

# Leer y desempaquetar cabecera WAVE
def leer_cabecera_wave(f):
    cabecera = f.read(44)
    if len(cabecera) != 44:
        raise ValueError("Cabecera del archivo WAVE incorrecta o incompleta.")
    return struct.unpack('<4sI4s4sIHHIIHH4sI', cabecera)

# Escribir cabecera WAVE
def escribir_cabecera_wave(f, cabecera):
    f.write(struct.pack('<4sI4s4sIHHIIHH4sI', *cabecera))

# Función para convertir estéreo a mono
def estereo2mono(ficEste, ficMono, canal=2):
    with open(ficEste, 'rb') as f:
        cabecera = leer_cabecera_wave(f)
        chunk_id, chunk_size, format, subchunk1_id, subchunk1_size, audio_format, num_channels, sample_rate, byte_rate, block_align, bits_per_sample, subchunk2_id, subchunk2_size = cabecera

        if chunk_id != b'RIFF' or format != b'WAVE' or subchunk1_id != b'fmt ' or subchunk2_id != b'data':
            raise ValueError("El archivo de entrada no es un archivo WAVE válido.")
        if num_channels != 2 or bits_per_sample != 16:
            raise ValueError("El archivo de entrada no es estéreo o no tiene 16 bits por muestra.")

        num_channels = 1
        byte_rate = sample_rate * num_channels * bits_per_sample // 8
        block_align = num_channels * bits_per_sample // 8
        subchunk2_size = subchunk2_size // 2
        chunk_size = 36 + subchunk2_size

        nueva_cabecera = (chunk_id, chunk_size, format, subchunk1_id, subchunk1_size, audio_format, num_channels, sample_rate, byte_rate, block_align, bits_per_sample, subchunk2_id, subchunk2_size)

        with open(ficMono, 'wb') as out_f:
            escribir_cabecera_wave(out_f, nueva_cabecera)
            while True:
                datos = f.read(4)
                if not datos:
                    break
                muestra_izq, muestra_der = struct.unpack('<hh', datos)
                if canal == 0:
                    muestra_mono = muestra_izq
                elif canal == 1:
                    muestra_mono = muestra_der
                elif canal == 2:
                    muestra_mono = (muestra_izq + muestra_der) // 2
                elif canal == 3:
                    muestra_mono = (muestra_izq - muestra_der) // 2
                else:
                    raise ValueError("Canal no válido. Debe ser 0, 1, 2 o 3.")
                out_f.write(struct.pack('<h', muestra_mono))

# Función para convertir mono a estéreo
def mono2estereo(ficL, ficR, ficEste):
    with open(ficL, 'rb') as f_izq:
        cabecera_izq = leer_cabecera_wave(f_izq)
    if ficR:
        with open(ficR, 'rb') as f_der:
            cabecera_der = leer_cabecera_wave(f_der)
        if cabecera_izq != cabecera_der:
            raise ValueError("Los archivos mono no tienen la misma configuración.")
    else:
        cabecera_der = cabecera_izq

    chunk_id, chunk_size, format, subchunk1_id, subchunk1_size, audio_format, num_channels, sample_rate, byte_rate, block_align, bits_per_sample, subchunk2_id, subchunk2_size = cabecera_izq

    num_channels = 2
    byte_rate = sample_rate * num_channels * bits_per_sample // 8
    block_align = num_channels * bits_per_sample // 8
    subchunk2_size = subchunk2_size * 2 if ficR else subchunk2_size * 2
    chunk_size = 36 + subchunk2_size

    nueva_cabecera = (chunk_id, chunk_size, format, subchunk1_id, subchunk1_size, audio_format, num_channels, sample_rate, byte_rate, block_align, bits_per_sample, subchunk2_id, subchunk2_size)

    with open(ficEste, 'wb') as out_f:
        escribir_cabecera_wave(out_f, nueva_cabecera)
        with open(ficL, 'rb') as f_izq, (open(ficR, 'rb') if ficR else open(ficL, 'rb')) as f_der:
            f_izq.seek(44)
            f_der.seek(44)
            while True:
                datos_izq = f_izq.read(2)
                datos_der = f_der.read(2)
                if not datos_izq or not datos_der:
                    break
                muestra_izq = struct.unpack('<h', datos_izq)[0]
                muestra_der = struct.unpack('<h', datos_der)[0]
                datos_estereo = struct.pack('<hh', muestra_izq, muestra_der)
                out_f.write(datos_estereo)

# Main function
if __name__ == "__main__":
    args = docopt(doc, version='estereo 1.0')

    if args['mono']:
        ficEste = args['ficEste']
        ficMono = args['ficMono']

        if args['--left']:
            estereo2mono(ficEste, ficMono, canal=0)
        elif args['--right']:
            estereo2mono(ficEste, ficMono, canal=1)
        elif args['--diferencia']:
            estereo2mono(ficEste, ficMono, canal=3)
        else:
            estereo2mono(ficEste, ficMono, canal=2)
    else:
        ficL = args['ficL']
        ficR = args['ficR'] if 'ficR' in args else None
        ficEste = args['ficEste']

        mono2estereo(ficL, ficR, ficEste)
