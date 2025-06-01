"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    resultado = []
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 5:
                letra = parts[0]
                columna_4 = len(parts[3].split(','))
                columna_5 = len(parts[4].split(','))
                resultado.append((letra, columna_4, columna_5))

    return resultado