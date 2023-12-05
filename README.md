# Supuestos

## Book.py

class SQL:
    """
        se modifico un poco esta clase para poder visualizar los resultados de las operaciones
        se añadio un metodo llamado to_string que muestra la tabla books en un dataframe como tabla
    """

class Book:
    """
        clase que implementa las operaciones CRUD sobre la tabla deseada, asume que la tabla se llama books
        y que un libro siempre se trabaja con los campos title, author y year que pueden ser null, pero se deben
        especificar en ese orden
    """

## indexing.py

def multilevel_indexing(documents, keys):
    """
        func recursiva que recibe una lista de diccionarios y una lista de keys
        agrupa los diccionarios por la primera key y luego llama recursivamente
        a la funcion con la lista de diccionarios agrupados y las keys restantes
        hasta que no queden keys y retorne el resultado. asume que las keys vienen en
        orden de jerarquia
    """

## fizzbuzz.py

def fizzbuzz(n):
    """
        func que recibe un numero n y retorna una lista de numeros del 1 al n
        reemplazando los multiplos de 3 por Fizz, los multiplos de 5 por Buzz
        y los multiplos de 3 y 5 por FizzBuzz
    """