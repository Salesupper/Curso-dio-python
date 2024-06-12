class Pessoa:
    def __init__(self,nome=None,idade=None):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_pelo_nascimento(cls,ano,mes,dia,nome):
        idade = 2024 - ano
        return cls(nome,idade)

    @staticmethod
    def eh_maior_18(idade):
        return idade >= 18

# pessoa1 = Pessoa('carlos',47)

p2 = Pessoa.criar_pelo_nascimento(2003,15,27,'gabiru')
print(p2.nome, p2.idade)

print(Pessoa.eh_maior_18(p2.idade))
print(Pessoa.eh_maior_18(12))