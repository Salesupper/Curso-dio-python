curso = "curso de Python"
nome_curso = curso
saldo,limite = 200,200

#ocupam mesma região de memoria
print(curso is nome_curso) 
print(curso is not nome_curso)
print(saldo is limite)