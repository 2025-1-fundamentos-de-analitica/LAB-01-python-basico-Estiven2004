"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    with open('files/input/data.csv') as file:
        registros = {}
        for line in file:
            columns = line.strip().split('\t')
            if len(columns) > 1:
                letra = columns[0]
                value = int(columns[1])
                if letra in registros:
                    registros[letra][0] = max(registros[letra][0], value)
                    registros[letra][1] = min(registros[letra][1], value)
                else:
                    registros[letra] = [value, value]

    return sorted([(letra, values[0], values[1]) for letra, values in registros.items()])