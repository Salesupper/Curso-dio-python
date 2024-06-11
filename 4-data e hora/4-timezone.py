from datetime import datetime as dt
import pytz

# da pra 
data = dt.now(pytz.timezone('Europe/Oslo'))
data_sp = dt.now(pytz.timezone('America/Sao_Paulo'))

print(data)
print(data_sp)