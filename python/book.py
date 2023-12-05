import pandas as pd

class SQL:
    """
        se modifico un poco esta clase para poder visualizar los resultados de las operaciones
        se añadio un metodo llamado to_string que muestra la tabla books en un dataframe como tabla
    """

    seq = 0

    books = {}

    def create(self, table_name="books", *args, **kwargs):
        print("Creando registro nuevo")
        print(table_name)
        print(args)
        print(kwargs)
        SQL.seq += 1
        self.books[SQL.seq] = {'title': args(0),
                               'author': args(1),
                               'year': args(2)} if len(args) > 0 else kwargs
        return SQL.seq

    def update(self, record_id, table_name="books", *args, **kwargs):
        print(f"Actulizando {table_name} con id: {record_id}")
        print(f"Valores: {args}")
        print(kwargs)
        self.books[record_id] = {'title': args(0),
                                 'author': args(1),
                                 'year': args(2)} if len(args) > 0 else kwargs

    def list(self, table_name="books"):
        print(f"Lista de {table_name}")

    def retrieve(self, record_id, table_name="books"):
        print(f"Se obtiene {record_id} desde {table_name}")
        print(self.books[record_id])

    def delete(self, record_id, table_name="books"):
        print(f"Se elimino {record_id} desde {table_name}")
        del self.books[record_id]

    def to_string(self):
        print("Imprimiendo tabla books")
        print(pd.DataFrame.from_dict(self.books, orient='index'))


class Book:
    """Aquí implementar la clase"""
    """
        clase que implementa las operaciones CRUD sobre la tabla deseada, asume que la tabla se llama books
        y que un libro siempre se trabaja con los campos title, author y year que pueden ser null, pero se deben
        especificar en ese orden
    """

    def get(self, id):
        db = SQL()
        try:
            book = db.retrieve(id)
        except Exception as e:
            print(f'Error retrieving book: {e}')
            book = -1
        finally:
            print('db connection closed')
        return book

    def create(self, title, author, year):
        db = SQL()
        try:
            id = db.create(title=title, author=author, year=year)
        except Exception as e:
            print(f'Error creating book: {e}')
            id = -1
        finally:
            print('db connection closed')
        return id

    def update(self, id, title, author, year):
        db = SQL()
        try:
            if db.retrieve(id) != -1:
                db.update(id, title=title, author=author, year=year)
            else:
                print(f'Book with id {id} does not exist, creating new book')
                id = db.create(title, author, year)
        except Exception as e:
            print(f'Error updating book: {e}')
        finally:
            print('db connection closed')

    def delete(self, id):
        db = SQL()
        try:
            if db.retrieve(id) != -1:
                db.delete(id)
            else:
                print(f'Book with id {id} does not exist')
        except Exception as e:
            print(f'Error deleting book: {e}')
        finally:
            print('db connection closed')


if __name__ == "__main__":
    db = SQL()
    book = Book()

    print()
    i = book.create("El Aleph", "Jorge L. Borges", 1949)
    print(i)
    print()
    i = book.create("La ciudad y los perros", "Mario Vargas Llosa", 1963)
    print(i)

    print()
    db.to_string()
    print()
    book.update(1, "El Aleph - edicion 2", "Jorge Luis Borges", 1949)
    print()

    book.update(2, "Necronomicon", "H.P. Lovecraft", 1927)
    print()

    book.delete(2)
    print()

    book.get(0)
    print()

    book.delete(-1)
    print()

    book.update(-3, "El Aleph - edicion", "Jorge Luis Borges", 3)

    db.to_string()
