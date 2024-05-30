menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
saques = 0
LIMITE_SAQUES = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        deposito = float(input("digite o valor do depósito R$"))
        
        if deposito <= 0:
            print("deposito invalido tente novamente")
        else:
            extrato += f"Depósito: R$ {deposito:.2f}\n"
            saldo += deposito

    elif opcao == "s":
        if saques >= LIMITE_SAQUES:
            print("limite de saques atingido")
        
        else:
            valor = float(input("digite o valor do saque R$"))
        
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

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")  
        print("==========================================")
       
    elif opcao == "q":
        print("\noperação encerrada")
        break
    
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
