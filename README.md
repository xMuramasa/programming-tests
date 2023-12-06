# Supuestos

### Observaciones

Para este desafío, se incluyen metodos sin pandas en los archivos:

- ```book_no_pandas.py```
- ```indexing_no_pandas.py```

Para todos los casos los supuestos son los mismos que en el caso que usa pandas

## Book.py

```python
class SQL:

    """
        se modifico un poco esta clase para poder visualizar los resultados de las operaciones
    """

class Book:

    """
        clase que implementa las operaciones CRUD sobre la tabla deseada,
        asume que la tabla se llama books y que un libro siempre se trabaja
        con los campos title, author y year que pueden ser null, pero se deben
        especificar en ese orden
    """
```

## indexing.py

```python
def multilevel_indexing(documents, keys):

    """
        func recursiva que recibe una lista de diccionarios y una lista de keys
        agrupa los diccionarios por la primera key y luego llama recursivamente
        a la funcion con la lista de diccionarios agrupados y las keys restantes
        hasta que no queden keys y retorne el resultado.
        Asume que las keys vienen en orden de jerarquia
    """
```

## fizzbuzz.py

```python
def fizzbuzz(n):

    """
        func que recibe un numero n y retorna una lista de numeros del 1 al n
        reemplazando los multiplos de 3 por Fizz, los multiplos de 5 por Buzz
        y los multiplos de 3 y 5 por FizzBuzz
    """
```
