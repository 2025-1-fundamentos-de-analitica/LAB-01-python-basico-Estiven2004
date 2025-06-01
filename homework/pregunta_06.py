"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
    max_min_por_clave = {}
    with open('files/input/data.csv', 'r') as file:
        for line in file:
            parts = line.strip().split('\t')
            if len(parts) >= 5:  
                diccionario_str = parts[4]
                pares = diccionario_str.split(',')
                for par in pares:
                    if ':' in par:
                        clave, valor_str = par.split(':')
                        valor = int(valor_str)
                        if clave in max_min_por_clave:
                            max_min_por_clave[clave][0] = min(max_min_por_clave[clave][0], valor)
                            max_min_por_clave[clave][1] = max(max_min_por_clave[clave][1], valor)
                        else:
                            max_min_por_clave[clave] = [valor, valor]

    lista_ordenada = sorted([(clave, valores[0], valores[1]) for clave, valores in max_min_por_clave.items()])

    return lista_ordenada