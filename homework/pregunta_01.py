"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open("files/input/data.csv", "r") as file:
        total = 0
        for line in file:  
            columns = line.strip().split("\t")
            if len(columns) > 1:
                total += int(columns[1])
        return total
