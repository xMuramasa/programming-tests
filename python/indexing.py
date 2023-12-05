import pandas as pd
import json


def multilevel_indexing(documents, keys):
    """Aquí va la solución"""
    """
        func recursiva que recibe una lista de diccionarios y una lista de keys
        agrupa los diccionarios por la primera key y luego llama recursivamente
        a la funcion con la lista de diccionarios agrupados y las keys restantes
        hasta que no queden keys y retorne el resultado. asume que las keys vienen en
        orden de jerarquia    
    """

    df = pd.DataFrame(documents).groupby(keys[0])
    if len(keys) == 1:
        result = {id: item.to_dict('records') for id, item in df}
    else:
        result = {id: multilevel_indexing(item.to_dict('records'), keys[1:]) for id, item in df}
    return result


if __name__ == '__main__':
    objects = [
        {
            "age": 12,
            "name": "Mateo",
            "last_name": "Gonzalez",
        },
        {
            "age": 25,
            "name": "Arturo",
            "last_name": "Gonzalez",
        },
        {
            "age": 12,
            "name": "Julian",
            "last_name": "Fernandez",
        },
    ]

    keys = ["age", "last_name"]
    indexed_data = multilevel_indexing(objects, keys)

    # pretty print dict
    print(json.dumps(indexed_data, indent=2))
