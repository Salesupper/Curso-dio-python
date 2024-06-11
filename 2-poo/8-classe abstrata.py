from abc import ABC,abstractmethod,abstractproperty

# interfaces
# é obrigado a implementar os metodos da classe ControleRemoto
class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass
    
    @property
    @abstractproperty
    def marca(self):
        pass

class ControleTV(ControleRemoto):
    def ligar(self):
        print('tv ligada')

    def desligar(self):
        print('tv desligada')

    @property
    def marca(self):
        return 'TCL'

class Controle_ArCondicionado(ControleRemoto):
    def ligar(self):
        print('ligando ar...')
        print('ar frio')

    def desligar(self):
        print('desligando ar...')
        print('ar quente')

    @property
    def marca(self):
        return 'Samsung'

controle = ControleTV()
controle.ligar()
controle.desligar()
ar = Controle_ArCondicionado()
ar.ligar()
ar.desligar()
print(controle.marca)
print(ar.marca)