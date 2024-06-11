from datetime import date, datetime, time

data = date(2024, 7, 10)
print(data)
print(date.today())

# hora, min e seg são opcionais fica 00:00:00
data_hora = datetime(2024,2,12, 16,30,24)
print(data_hora)
print(data_hora.today())

hour = time(22,30,00)
print(hour)
