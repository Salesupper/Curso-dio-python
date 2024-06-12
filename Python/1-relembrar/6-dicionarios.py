pessoa = {'nome':'guilherme','idade':21}

pessoa['nome'] = 'adrielson'

amigos = {
    '001':{'nome':'guilherme','idade':21},
    '002':{'nome':'victor','idade':19},                            
    '003':{'nome':'gilberto','idade':32}}    

# print(pessoa['nome'])
# print(pessoa)
# pessoa['contato'] = '4002-8922'

# print(amigos['002'])
# print(amigos['003']['nome'])

# for chave in amigos:
#     print(chave, amigos[chave])

# for chave,valor in amigos.items():
#     print(chave, valor)

# dict.fromkeys(['nome','telefone'])
# dict.fromkeys(['nome','telefone'],'vazio')

print(pessoa.values())
print(pessoa.keys())
print(pessoa.items()) #print(pessoa)
print(pessoa.get('nome'))

# carros = {
#     'marcas':['vw','fiat','renault','mercedes','chevrolet'],
#     'motor':[1.0,2.0,3.0,4.0,5.0,6.0]}

# print(f"Marca: {carros['marcas'][1]}, Motor: {carros['motor'][2]}")
