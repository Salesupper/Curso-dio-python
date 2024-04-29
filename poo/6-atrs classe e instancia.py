class Estudante:
    # variavel de classe
    escola = 'dio'

    # variavel de instância
    def __init__(self,nome,matricula):
        self.nome = nome
        self.matricula = matricula

    def __str__(self) -> str:
        return f'{self.nome} - {self.matricula} - {self.escola}'

def exibir(*objs):
    for obj in objs:
        print(obj)

e1 = Estudante('joao',1)
e2 = Estudante('maria',2)

exibir(e1,e2)
e1.matricula = 3
Estudante.escola = 'impacta'
e3 = Estudante('mauro',4)
e3.escola = 'Fiap'
exibir(e1,e2,e3)

