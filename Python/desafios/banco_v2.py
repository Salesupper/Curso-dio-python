def sacar(*,saldo,valor,extrato,limite,saques,LIMITE_SAQUES):
    if saques >= LIMITE_SAQUES:
        print("limite de saques atingido")
    else:
        if valor > saldo:
            print("saldo insuficiente para saque")
        elif valor <= 0:
            print("saldo inválido para saque")
        elif valor > limite:
            print("saque disponível apenas para valores até R$500,00")
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            saques += 1
    return saldo,extrato,saques


def depositar(saldo,deposito,extrato,/):
    if deposito <= 0:
        print("deposito inválido tente novamente")
    else:
        extrato += f"Depósito: R$ {deposito:.2f}\n"
        saldo += deposito
    return saldo,extrato


def mostrar_extrato(saldo,/,*,extrato,):
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")  
    print("==========================================")


def criar_usuario(usuarios):
    usuario = {'nome':'','cpf':'','contas':[]}
    nome = str(input('digite o nome: '))
    cpf = input('digite o cpf: ')
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print('usuario já existente')
            return
    nasc = str(input('digite a data do nascimento(dd/mm/aaaa): '))
    endereço = str(input('digite o endereço: '))
    usuario = {'nome':nome,'cpf':cpf,'contas':[]}
    usuarios.append(usuario)
    print('\n-=-=-= Usuário Criado =-=-=-')


def criar_conta(usuarios,AGENCIA):
    for u in enumerate(usuarios):
        print(u)
    n = int(input('digite o num do usuario que deseja criar conta: '))
    num_conta = int(input('digite o num da conta que deseja criar: '))
    conta = {'agencia':AGENCIA,'num_conta':num_conta}
    usuarios[n]['contas'].append(conta)
    print('\n-=-=-= Conta Criada =-=-=-')


menu = """

[ca] Criar Usuário
[cc] Criar Conta
[lu] Listar Usuarios
[d]  Depositar
[s]  Sacar
[e]  Extrato
[q]  Sair

=> """

LIMITE_SAQUES = 3
AGENCIA = '0001'
saldo = 0
limite = 500
extrato = ""
saques = 0
usuarios = []

while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("digite o valor do depósito R$"))
        saldo,extrato = depositar(saldo,deposito,extrato)
        
    elif opcao == "s":
        valor = float(input("digite o valor do saque R$"))
        saldo,extrato,saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                saques=saques,
                LIMITE_SAQUES=LIMITE_SAQUES)
        
    elif opcao == "e":
        mostrar_extrato(saldo,extrato=extrato)

    elif opcao == "ca":
        criar_usuario(usuarios)

    elif opcao == "cc":
        criar_conta(usuarios,AGENCIA)

    elif opcao == "lu":
        for u in enumerate(usuarios):
            print(u)

    elif opcao == "q":
        print("\noperação encerrada")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

