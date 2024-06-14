import sqlite3 as sq
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sq.connect(ROOT_PATH / 'my_bank.db')
cursor = conexao.cursor()


def criar_tabela(conexao,cursor):
    cursor.execute('''
        CREATE TABLE clientes(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome VARCHAR(100),
        email VARCHAR(150))'''
    )
    conexao.commit()


def inserir_dados(conexao, cursor, nome, email):
    data = (nome,email)
    cursor.execute('''
        INSERT INTO clientes (nome,email) 
        VALUES (?,?);''',data)
    # envia os dados para a tabela
    conexao.commit()


def atualizar_dados(conexao,cursor,nome,email,id):
    data = (nome,email,id)
    cursor.execute('''
        UPDATE clientes 
        SET nome=?, email=? 
        WHERE id=?;''',data
    )
    conexao.commit()
    

def deletar_dados(conexao,cursor,id):
    data = (id,)
    cursor.execute('''
        DELETE FROM clientes 
        WHERE id=?;''',data
    )
    conexao.commit()


def inserir_muitos(conexao,cursor,dados):
    cursor.executemany('''
        INSERT INTO clientes (nome,email)
        VALUES (?,?);''',dados
    )
    conexao.commit()

# deletar_dados(conexao,cursor,2)
# atualizar_dados(conexao,cursor,'Marcos','marcos@gmail.com',1)

# #obrigatorio os dados ficarem em uma tupla
# lista = [
#     ('Geraldo','ge@gmail.com'),
#     ('Naldo','nal@canal.com.br'),
#     ('Jabson','jab22@hotmail.com')
#     ]

# inserir_muitos(conexao,cursor,lista)

############### Consultas SQL ###############

def retornar_cliente(cursor,id):
    cursor.execute('''
        SELECT * FROM clientes
        WHERE id=?''',(id,)
    )
    return cursor.fetchone()


def listar_clientes(cursor):
    return cursor.execute('''
        SELECT * FROM clientes
        ORDER BY nome'''
    )


# print(retornar_cliente(cursor,1))
# clientes = listar_clientes(cursor)
# for cliente in clientes:
#     print(cliente)