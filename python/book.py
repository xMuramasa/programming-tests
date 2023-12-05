import pandas as pd

class SQL:
    """
        se modifico un poco esta clase para poder visualizar los resultados de las operaciones
        se añadio un metodo llamado to_string que muestra la tabla books en un dataframe como tabla
    """

    seq = 0

    books = pd.DataFrame({'title': ['L0'], 'author': ['A0'], 'year': [0]})

    def create(self, table_name="books", *args, **kwargs):
        print("Creando registro nuevo")
        print(table_name)
        print(args)
        print(kwargs)
        SQL.seq += 1
        new_book = args if len(args) > 0 else list(kwargs.values())
        self.books.loc[self.seq] = new_book
        return SQL.seq

    def update(self, record_id, table_name="books", *args, **kwargs):
        print(f"Actulizando {table_name} con id: {record_id}")
        print(f"Valores: {args}")
        print(kwargs)
        update_book = args if len(args) > 0 else list(kwargs.values())
        self.books.loc[record_id] = update_book

    def book_list(self, table_name="books"):
        print(f"Lista de {table_name}")
        return self.books.to_dict('records')

    def retrieve(self, record_id, table_name="books"):
        if record_id not in self.books.index:
            return {}
        print(f"Se obtiene {record_id} desde {table_name}")
        return self.books.iloc[record_id].to_dict()

    def delete(self, record_id, table_name="books"):
        print(f"Se elimino {record_id} desde {table_name}")
        self.books.drop(record_id, inplace=True)

    def to_string(self):
        print("Imprimiendo tabla books")
        print(self.books)


class Book:
    """
        clase que implementa las operaciones CRUD sobre la tabla deseada, asume que la tabla se llama books
        y que un libro siempre se trabaja con los campos title, author y year que pueden ser null, pero se deben
        especificar en ese orden
    """

    def get(self, id=None):
        db = SQL()
        try:
            if id is not None:
                books = db.retrieve(id)
            else:
                books = db.book_list()
        except Exception as e:
            print(f'Error retrieving book: {e}')
            books = None
        finally:
            print('db connection closed')
        return books

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
            if db.retrieve(id) != {}:
                db.update(record_id=id, title=title, author=author, year=year)
            else:
                print(f'Book with id {id} does not exist, creating new book')
                id = db.create('books', title, author, year)
        except Exception as e:
            print(f'Error updating book: {e}')
        finally:
            print('db connection closed')

    def delete(self, id):
        db = SQL()
        try:
            if db.retrieve(id) != {}:
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
    i = book.create("L1", "A1", 1)
    print(i)
    print()
    i = book.create("L2", "A2", 3)
    print(i)

    print()
    db.to_string()
    print()
    book.update(1, "L1 - edicion", "A1 - edicion", 2)
    print()

    book.update(3, "L3", "A3", 12)
    print()

    book.delete(2)
    print()

    print(book.get(0))
    print()

    book.delete(-1)
    print()

    print(book.get())
    print()

    book.update(-3, "AAA", "BBB", 3)

    db.to_string()
