class SQL:

    seq = 0

    def create(self, table_name="books", *args, **kwargs):
        print("Creando registro nuevo")
        print(table_name)
        print(args)
        print(kwargs)
        SQL.seq += 1
        return SQL.seq

    def update(self, record_id, table_name="books", *args, **kwargs):
        print(f"Actulizando {table_name} con id: {record_id}")
        print(f"Valores: {args}")
        print(kwargs)

    def list(self, table_name="books"):
        print(f"Lista de {table_name}")

    def retrieve(self, record_id, table_name="books"):
        print(f"Se obtiene {record_id} desde {table_name}")

    def delete(self, record_id, table_name="books"):
        print(f"Se elimino {record_id} desde {table_name}")



class Book:
    """Aquí implementar la clase"""


