curso = '  python '
word = 'banco'

# deixar letras maisculas ou minusculas
print(word.upper())
print(word.lower())
print(word.title())

# remover espaços
print(curso.lstrip())
print(curso.rstrip())
print(curso.strip())

# junção e centralização
print(word.center(9,'#'))
print('-'.join(word))