# saber ano atual
from datetime import datetime as dt 

atual = dt.now().year
print(atual)

class Pessoa:
    def __init__(self,nome,ano_nasc):
        self._nome = nome
        self._ano_nasc = ano_nasc

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def name(self,name):
        self._nome = name

    @property
    def idade(self):
        ano_atual = 2024
        return ano_atual - self._ano_nasc 

    #funciona da mesma forma
    def get_nome(self):
        return self._nome

    def get_idade(self):
        return 2024 - self._ano_nasc
    
joao = Pessoa('joao',2003)

print(f'Nome: {joao.nome}')
print(joao.idade,'anos')
print(f'Nome: {joao.get_nome()}')