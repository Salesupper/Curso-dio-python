from pathlib import Path

ROOT_PATH = Path(__file__).parent

'1-usar o with'

'''sem o with é necessario ficar fechando com o close'''
# arq = open(ROOT_PATH/'lore.txt','r')
# print(arq.read())
# arq.close()

'''com o with isso é automatizado
porem tem de se manter identado
senão o arquivo estará fechado'''

# with open(ROOT_PATH/'lore.txt','r') as arq:
#     print(arq.read())

'2-verificar se o arquivo foi aberto com sucesso'

# try:
#     with open(ROOT_PATH/'lorei.txt','r') as arq:
#         print(arq.read())
# except IOError as exc:
#     print(f'erro ao abrir o arquivo {exc}')

'3-usar a codificação correta'

try:
    with open(ROOT_PATH/'arquivo-utf-8.txt','w',encoding='utf-8') as arq:
        arq.write('aprendendo a manipular arquivos utilizando python')
except IOError as exc:
    print(f'erro ao abrir o arquivo {exc}')