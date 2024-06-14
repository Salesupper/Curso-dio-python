import sqlite3 

con = sqlite3.connect('DBapi_python\my_bank.db')
cursor = con.cursor()

# retorna em dicionario
cursor.row_factory = sqlite3.Row


def listar_clientes(cursor):
    return cursor.execute('''
        SELECT * FROM clientes
        ORDER BY id'''
    )


clientes = listar_clientes(cursor)
for cliente in clientes:
    # print(dict(cliente))
    print(cliente['id'], cliente['nome'], cliente['email'])
