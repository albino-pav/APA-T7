"""
Autores: Ivan Enciso y Pau Codina
Descripción: Normalización de expresiones horarias en un texto.
"""

import re

def normalizaHoras(ficText, ficNorm):
    """
    Lee el fichero de texto ficText, lo analiza en busca de expresiones horarias y escribe el fichero ficNorm
    en el que éstas se expresan según el formato normalizado, con las horas y los minutos indicados por dos dígitos
    y separados por dos puntos (08:27).
    """
    def normaliza_hora(match):
        hora, minutos = match.groups()
        return f"{int(hora):02}:{int(minutos):02}"

    with open(ficText, 'r') as f_in, open(ficNorm, 'w') as f_out:
        for line in f_in:
            # Normalizar 8h27m
            line = re.sub(r'\b(\d{1,2})h(\d{1,2})m\b', normaliza_hora, line)
            # Normalizar 8 en punto
            line = re.sub(r'\b(\d{1,2}) en punto\b', lambda m: f"{int(m.group(1)):02}:00", line)
            # Normalizar 8 y cuarto
            line = re.sub(r'\b(\d{1,2}) y cuarto\b', lambda m: f"{int(m.group(1)):02}:15", line)
            # Normalizar 8 y media
            line = re.sub(r'\b(\d{1,2}) y media\b', lambda m: f"{int(m.group(1)):02}:30", line)
            # Normalizar 8 menos cuarto
            line = re.sub(r'\b(\d{1,2}) menos cuarto\b', lambda m: f"{int(m.group(1))-1:02}:45", line)
            # Normalizar ... de la mañana/tarde/noche/madrugada/mediodía
            line = re.sub(r'\b(\d{1,2}) de la (mañana|tarde|noche|madrugada|mediodía)\b', normaliza_periodo, line)
            f_out.write(line)

def normaliza_periodo(match):
    hora, periodo = match.groups()
    hora = int(hora)
    if periodo == 'mañana':
        if hora == 12: hora = 0
        return f"{hora:02}:00"
    elif periodo == 'tarde':
        if 1 <= hora <= 11:
            return f"{hora+12:02}:00"
        else:
            return match.group(0)
    elif periodo == 'noche':
        if 8 <= hora <= 11 or hora == 12:
            return f"{hora%12:02}:00"
        elif 1 <= hora <= 7:
            return f"{hora+12:02}:00"
        else:
            return match.group(0)
    elif periodo == 'madrugada':
        if 1 <= hora <= 6:
            return f"{hora:02}:00"
        else:
            return match.group(0)
    elif periodo == 'mediodía':
        if 1 <= hora <= 3:
            return f"{hora+12:02}:00"
        else:
            return match.group(0)

if __name__ == '__main__':
    normalizaHoras('horas.txt', 'horas_norm.txt')
