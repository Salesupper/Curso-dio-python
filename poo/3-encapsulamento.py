class Conta:
    def __init__(self,num_conta,saldo=0):
        self._saldo = saldo
        self.num_conta = num_conta

    def get_saldo(self):
        return self._saldo

    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self,valor):
        if valor <= self._saldo:
            self._saldo -= valor

c1 = Conta('001')
c1.depositar(2000)
c1.sacar(500)
print(c1.num_conta)
print(c1.get_saldo())






