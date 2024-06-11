def calculadora(operacao):
    def soma(a,b):
        return a + b
    
    def sub(a,b):
        return a - b

    def div(a,b):
        return a / b

    def mult(a,b):
        return a * b

    # Exemplo slide
    # if operacao == '+':
    #     return soma
    
    match operacao:
        case '+':
            return soma
        case '-':
            return sub
        case '/':
            return div
        case '*':
            return mult

print(calculadora('+')(2,2))
print(calculadora('-')(8,4))
op = calculadora('/')(12,2)
print(op)
x = calculadora('*')
print(x(4,4))