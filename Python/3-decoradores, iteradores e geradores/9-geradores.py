# def gerador():
#     yield 1

# def gerador():
#     texto = 'python'
#     yield texto

def gerador(lista: list[int]):
    for num in lista:
        yield num * 2
        

for i in gerador(lista=[12,2,4]):
    print(i)