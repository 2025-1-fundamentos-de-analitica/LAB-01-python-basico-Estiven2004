"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
    suma_por_letra = {}
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 4:
                letras_columna_4 = parts[3].split(',')
                valor_columna_2 = int(parts[1])
                
                for letra in letras_columna_4:
                    if letra in suma_por_letra:
                        suma_por_letra[letra] += valor_columna_2
                    else:
                        suma_por_letra[letra] = valor_columna_2

    return dict(sorted(suma_por_letra.items()))