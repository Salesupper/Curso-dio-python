def msg(nome='marcio'):
    print(f'ola {nome}')

msg()
msg(nome='lucas')

numbers = [7,5,4,3]

def somar(nums):
    return sum(nums)

print(somar(numbers))
print(somar([1,2,3,4]))

def salvar_carro(marca,modelo,ano,placa):
    print(f'carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}')

# salvar_carro('Fiat','Palio',2001,'ABC-1234')
# salvar_carro(marca='Fiat',modelo='Palio',ano=2001,placa='ABC-1234')

# # ** para receber um dicionario (kwargs)
# salvar_carro(**{'marca':'Fiat','modelo':'Palio','ano':2001,'placa':'ABC-1234'}) 

# # * para receber uma tupla (args)
# salvar_carro(*('Fiat','Palio',2001,'ABC-1234'))

salario = 2000

def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario

print(salario_bonus(300))

