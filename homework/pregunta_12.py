"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
    suma_por_letra = {}
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 5:  
                letra_columna_1 = parts[0]
                pares_columna_5 = parts[4].split(',')
                
                if letra_columna_1 not in suma_por_letra:
                    suma_por_letra[letra_columna_1] = 0
                
                for par in pares_columna_5:
                    clave_valor = par.split(':')
                    if len(clave_valor) == 2:
                        valor = int(clave_valor[1])
                        suma_por_letra[letra_columna_1] += valor

    return suma_por_letra