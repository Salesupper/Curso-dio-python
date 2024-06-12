import os
import shutil as st
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# cria a pasta abaixo na raiz no projeto
# os.mkdir('novo-diretorio')

'''
cria a pasta abaixo dentro da pasta 
que está o arquivo pai
'''
# os.mkdir(ROOT_PATH / 'novo-diretorio')

# arq = open(ROOT_PATH / 'new.txt', 'w')
# arq.close()

# renomear arquivo
# os.rename(ROOT_PATH/'new.txt', ROOT_PATH/'modified.txt')

# remover arquivo
# os.remove(ROOT_PATH/'modified.txt')

# move o arquivo
# st.move(ROOT_PATH/'new.txt', ROOT_PATH/'novo-diretorio'/'new.txt')

