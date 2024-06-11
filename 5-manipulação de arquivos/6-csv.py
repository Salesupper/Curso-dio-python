import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# escrita csv

# try:
#     with open(ROOT_PATH / 'usuarios.csv','w',encoding='utf-8',newline='') as arq:
#         escritor = csv.writer(arq)
#         escritor.writerow(['id', 'nome'])
#         escritor.writerow(['1', 'Marcos'])
#         escritor.writerow(['2', 'Jackson'])
# except IOError as exc:
#     print(f'erro ao criar o arquivo. {exc}')

# leitura csv

# try:
#     with open(ROOT_PATH / 'usuarios.csv','r',encoding='utf-8') as arq:
#         leitor = csv.reader(arq)
#         for linha in leitor:
#             print(linha)
# except IOError as exc:
#     print(f'erro ao criar o arquivo. {exc}')

# leitura modo dicionário

try:
    with open(ROOT_PATH / 'usuarios.csv','r',encoding='utf-8') as arq:
        leitor = csv.DictReader(arq)
        # print(leitor.fieldnames)
        for linha in leitor:
            print(f"ID: {linha['id']}")
            print(f"Nome: {linha['nome']}")
except IOError as exc:
    print(f'erro ao criar o arquivo. {exc}')