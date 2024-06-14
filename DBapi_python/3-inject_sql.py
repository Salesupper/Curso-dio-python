import sqlite3
from pathlib import Path

ROOT_PATH = Path(__file__).parent

conexao = sqlite3.connect(ROOT_PATH / "my_bank.db")
cursor = conexao.cursor()
cursor.row_factory = sqlite3.Row

'''
############# Atenção #############
modo errado de realizar a busca concatenando variáveis
o código fica vulnerável
'''

id_cliente = input("Informe o id do cliente: ")
cursor.execute(f"SELECT * FROM clientes WHERE id={id_cliente}")

clientes = cursor.fetchall()

for cliente in clientes:
    print(dict(cliente))