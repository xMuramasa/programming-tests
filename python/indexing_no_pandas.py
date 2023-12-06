import json

def dict_groupby(obj, key):
    """
        func que recibe una lista de diccionarios (obj) y el nombre de una
        llave de diccionario (key), que
        agrupa los valores de cada diccionario de la lista por la key
        y retorna un diccionario con los valores agrupados segun corresponda
    """
    result_dict = {}
    for item in obj:
        if item[key] not in result_dict:
            result_dict[item[key]] = [item]
        else:
            result_dict[item[key]].append(item)
    return result_dict

def multilevel_indexing(documents, keys):
    """
        func recursiva que recibe una lista de diccionarios y una lista de keys
        agrupa los diccionarios por la primera key y luego llama recursivamente
        a la funcion con la lista de diccionarios agrupados y las keys restantes
        hasta que no queden keys y retorne el resultado. asume que las keys vienen en
        orden de jerarquia    
    """
    data = dict_groupby(documents, keys[0])
    if len(keys) == 1:
        result = {id: item for id, item in data.items()}
    else:
        result = {id: multilevel_indexing(item, keys[1:]) for id, item in data.items()}
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
