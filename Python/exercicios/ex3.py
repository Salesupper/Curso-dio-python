import re

'''
    \(\d{2}\) corresponde aos dois dígitos dentro dos parênteses.
    9 corresponde ao dígito "9".
    \d{4} corresponde a quatro dígitos.
    - corresponde ao caractere de hífen.
    \d{4} corresponde a mais quatro dígitos.
'''

def validate_numero_telefone(phone_number):
    regex = r'^\(\d{2}\) 9\d{4}-\d{4}$'
    if re.match(regex, phone_number):  
        return 'Número de telefone válido.'
    else:
        return 'Número de telefone inválido.'

phone_number = input()  

result = validate_numero_telefone(phone_number)

print(result)