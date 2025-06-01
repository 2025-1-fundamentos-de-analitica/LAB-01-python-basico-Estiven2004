"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordenadas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    with open('files/input/data.csv') as file:
        registro = {}
        for line in file:
            columns = line.strip().split('\t')
            if len(columns) > 1:
                letra = columns[0]
                if letra in registro:
                    registro[letra] += int(columns[1])
                else:
                    registro[letra] = int(columns[1])
    return sorted(registro.items())
