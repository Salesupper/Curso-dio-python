# TODO: Crie a classe PlanoTelefone, seu método de inicialização e encapsule os atributos, 'nome' e 'saldo':
# TODO: Crie um método 'verificar_saldo' para verificar o saldo do plano sem acessar diretamente o atributo:    
# TODO: Crie um método 'mensagem_personalizada' para gerar uma mensagem personalizada com base no saldo: 


class PlanoTelefone:
    def __init__(self, nome_plano, saldo):
        self._nome_plano = nome_plano
        self._saldo = saldo

    @property
    def saldo(self):
        return self._saldo


# Classe UsuarioTelefone:
class UsuarioTelefone(PlanoTelefone):
    def __init__(self, nome, plano, saldo):
        super().__init__(nome_plano, saldo)
        self.nome = nome
        self.plano = plano

# TODO: Crie um método para verificar o saldo do usuário e gerar uma mensagem personalizada:
    def verificar_saldo(self, saldo):
        if saldo < 10:
            return "Seu saldo está baixo. Recarregue e use os serviços do seu plano."
        elif saldo >= 50:
            return "Parabéns! Continue aproveitando seu plano sem preocupações."
        else:
            return "Seu saldo está razoável. Aproveite o uso moderado do seu plano."
 
# Recebendo as entradas do usuário (nome, plano, saldo):
nome_usuario = input()
nome_plano = input()
saldo_inicial = float(input())

# Criação de objetos do plano de telefone e usuário de telefone com dados fornecidos:
plano_usuario = PlanoTelefone(nome_plano, saldo_inicial) 
usuario = UsuarioTelefone(nome_usuario, plano_usuario, saldo_inicial)  

# Chamada do método para verificar_saldo sem acessar diretamente os atributos do plano:
mensagem_usuario = usuario.verificar_saldo(saldo_inicial)  
print(mensagem_usuario)