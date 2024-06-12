from datetime import date, timedelta, datetime as dt

tipo_carro = 'm'

tempo_pequeno = 30
tempo_medio = 45
tempo_grande = 2
data_atual = dt.now()

if tipo_carro == 'p':
    estimado = data_atual + timedelta(minutes=tempo_pequeno)
    print(f"""Chegada: {data_atual} - Previsão Saída: {estimado}""")
elif tipo_carro == 'm':
    estimado = data_atual - timedelta(minutes=tempo_medio)
    print(f"""Chegada: {data_atual} - Previsão Saída: {estimado}""")
else:
    estimado = data_atual + timedelta(days=tempo_grande)
    print(f"""Chegada: {data_atual} - Previsão Saída: {estimado}""")

print(date.today() - timedelta(days=1))

resultado = dt(2024,7,9, 10,40,20) - timedelta(hours=1)
print(resultado.time())

print(dt.now().date())