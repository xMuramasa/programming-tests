# Tests de programación con Python

Este test consta de 3 preguntas para medir conocimientos en programación y el uso de `python`.

## Pregunta 1: FizzBuzz

Para este problema se pide que se desarrollé un programa y/o función en `python` que para todos los números del `1` al `100` entregue la palabra `"Fizz"` si el número es divisible por `3` y que entregue la palabra `"Buzz"` si es divisible por `5`, en caso de que el número sea divisible por `3` y `5` al mismo tiempo debe entregar la palabra `"FizzBuzz"`

## Pregunta 2: ORM simple

La idea de esta pregunta es desarrollar una parte de las tareas que cumple un `ORM` (Object Relation Mapper), para esto se pide que se desarrolle una clase en `python` llamada `Book` que permita crear objetos, guardarlos en la base de datos y actualizarlos, tendrá como base una clase llamada `SQL` que se encargará de lo respectivo a comunicación y funcionalidad directa con la base de datos.

```python
class SQL:

    def create(self, table_name, *args, **kwargs):
        """Creates a new record in the table 'table_name' with the essential arguments in args and kwargs"""

    def update(self, table_name, record_id, *args, **kwargs):
        """Updates the record with id = 'record_id' in the table 'table_name' with the new args and kwargs """

    def delete(self, table_name, record_id, *args, **kwargs):
        """Deletes the record with id = 'record_id' from the table 'table_name'"""

    def list(self, table_name):
        """List all the records from the table 'table_name' """

    def retrieve(self, table_name, record_id):
        """Retrives a single record with id = 'record_id' """

```

Se parte del supuesto de que la tabla `books` tiene una columna `id` como `primary key` del la tabla para simplificar el desarrollo.


## Pregunta 3: Indices multinivel

Para este problema el objetivo es generar una estructura de datos a partir de un listado de documentos (diccionarios) con llaves con strings y valores simples (no con diccionarios anidados) el objetivo es crear una función que tome este listado y un listado con llaves de los documentos y genere un diccionario nuevo que agrupe los datos por los valores de esas llaves.

Un ejemplo de su uso sería:
```python
def multilevel_index(documents, keys):
    """Implementación"""

objects = [
    {
        "age": 12,
        "name": "Mateo",
        "last_name": "González",
    }, 
    {
        "age": 25,
        "name": "Arturo",
        "last_name": "González",
    }, 
    {
        "age": 12,
        "name": "Julián",
        "last_name": "Fernández",
    },
]

multilevel_index(objects, ["age", "last_name"])
# Retornará 
{
    12: {
        "González": [
                {
                    "age": 12,
                    "name": "Mateo",
                    "last_name": "González",
                }
        ],
        "Fernández": [  
                {
                    "age": 12,
                    "name": "Julián",
                    "last_name": "Fernández",
                }
        ],
    },
    25: {
        "González": [
            {
                "age": 25,
                "name": "Arturo",
                "last_name": "González",
            },
        ]
    }
}
                            
```

