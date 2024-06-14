import sqlite3 

con = sqlite3.connect('DBapi_python\my_bank.db')
cur = con.cursor()
cur.row_factory = sqlite3.Row


# não é possivel inserir um dado com id já existente
try:
    cur.execute('''
        INSERT INTO clientes (nome,email) 
        VALUES (?,?);''',('teste3','t3@gmail.com'))
    cur.execute('''
        INSERT INTO clientes (id,nome,email) 
        VALUES (?,?,?);''',(2,'teste4','t4@gmail.com'))
    con.commit()
except Exception as e:
    print(f'ocorreu um erro: {e}')
    con.rollback()
