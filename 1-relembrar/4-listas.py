# num = [10,50,99,3,5,2,26]
# pares = []

# for n in num:
#     if n % 2 == 0:
#         pares.append(n)

# print(pares)

# # outra forma com compression
# # primeiro n é o retorno
# pares = [n for n in num if n % 2 == 0] 
# quadrado = [q**2 for q in num]
# print(pares)
# print(quadrado)

# lista = ['python',60,20,30]
# l2 = []

# l2 = lista.copy()
# l2.extend([30,30,30])
# # l2.reverse()
# # l2.sort()
# # ls.len()

# print(lista.clear())
# print(l2.count(30))
# print(l2.index(60))
# print(l2.pop())
# print(l2.pop(0))
# print(l2.remove(60))
# print(l2)

carros = ['gol','celta','uno']

for indice,carro in enumerate(carros):
    print(f'{indice}: {carro}')
